from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from .models import (
    Diresaun, Pozisaun, Kategoria, Sub_Kategoria, Marka, 
    Tipu_Entrada, Rak, Supplier
)

# =========================================================================
# 1. FUNGSI UNTUK EXPORT PDF (Custom Action)
# =========================================================================

def export_as_pdf(modeladmin, request, queryset):
    """
    Action generik untuk mengekspor data terpilih ke format PDF.
    """
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{modeladmin.model.__name__}.pdf"'
    
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []
    
    # Ambil kolom yang ditampilkan di list_display admin
    columns = [c for c in modeladmin.list_display if c != 'actions']
    
    # Header Tabel
    data = [[field.replace('_', ' ').upper() for field in columns]]
    
    # Data Baris
    for obj in queryset:
        row = []
        for field in columns:
            # Ambil nilai atribut atau metode display
            attr = getattr(obj, field, None)
            if callable(attr):
                val = attr()
            else:
                val = attr if attr is not None else "-"
            row.append(str(val))
        data.append(row)
    
    # Buat Tabel PDF
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    elements.append(table)
    doc.build(elements)
    return response

export_as_pdf.short_description = "Export Selected to PDF"

# =========================================================================
# 2. BASE ADMIN CLASS (Scalable & Reusable)
# =========================================================================

class BaseAdmin(ImportExportModelAdmin):
    """
    Class dasar yang mewarisi ImportExportModelAdmin.
    Semua model akan memiliki fitur Import, Export (Excel/CSV), dan PDF secara otomatis.
    """
    # Tambahkan aksi export PDF
    actions = [export_as_pdf]
    
    # Konfigurasi tampilan standar
    list_per_page = 20
    ordering = ['-created_at']
    
    # Otomatis mengisi created_by dan updated_by
    def save_model(self, request, obj, form, change):
        if not change: # Jika membuat baru
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.updated_at = timezone.now()
        super().save_model(request, obj, form, change)
    
    # Soft Delete Action
    def soft_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.soft_delete(request.user)
        self.message_user(request, "Data berhasil dihapus (soft delete).")
    soft_delete_selected.short_description = "Soft Delete Selected"

    def restore_selected(self, request, queryset):
        for obj in queryset:
            obj.undelete()
        self.message_user(request, "Data berhasil dipulihkan.")
    restore_selected.short_description = "Restore Selected"

    # Tambahkan aksi soft delete ke list aksi
    def get_actions(self, request):
        actions = super().get_actions(request)
        # Tambahkan aksi kustom
        actions['soft_delete_selected'] = (self.soft_delete_selected, 'soft_delete_selected', "Soft Delete Selected")
        actions['restore_selected'] = (self.restore_selected, 'restore_selected', "Restore Selected")
        return actions

    # Filter default untuk hanya menampilkan data yang aktif (belum di soft delete)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if hasattr(self.model, 'active_objects'):
            return self.model.active_objects.all()
        return qs

# =========================================================================
# 3. RESOURCE UNTUK IMPORT/EXPORT (Opsional jika butuh kustomisasi kolom)
# =========================================================================

class GenericResource(resources.ModelResource):
    class Meta:
        skip_unchanged = True
        report_skipped = True

# =========================================================================
# 4. REGISTRASI MODEL
# =========================================================================

@admin.register(Diresaun)
class DiresaunAdmin(BaseAdmin):
    resource_class = GenericResource
    list_display = ['code', 'name', 'created_at', 'updated_at', 'created_by']
    search_fields = ['code', 'name']

@admin.register(Pozisaun)
class PozisaunAdmin(BaseAdmin):
    resource_class = GenericResource
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']

@admin.register(Kategoria)
class KategoriaAdmin(BaseAdmin):
    resource_class = GenericResource
    list_display = ['name', 'created_at', 'created_by']
    search_fields = ['name']

@admin.register(Sub_Kategoria)
class Sub_KategoriaAdmin(BaseAdmin):
    resource_class = GenericResource
    list_display = ['name', 'kat', 'created_at']
    list_filter = ['kat']
    search_fields = ['name']

@admin.register(Marka)
class MarkaAdmin(BaseAdmin):
    resource_class = GenericResource
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Tipu_Entrada)
class TipuEntradaAdmin(BaseAdmin):
    resource_class = GenericResource
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Rak)
class RakAdmin(BaseAdmin):
    resource_class = GenericResource
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Supplier)
class SupplierAdmin(BaseAdmin):
    resource_class = GenericResource
    list_display = ['name', 'created_at']
    search_fields = ['name']

