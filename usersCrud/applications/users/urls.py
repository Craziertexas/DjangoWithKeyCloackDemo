from django.urls import path
from .views import Create_All_View, Detail_Mod_Delete_View

app_name = "users"

urlpatterns = [
    path('', Create_All_View.as_view(), name='All/Create'),
    path('<uuid:UUID>',Detail_Mod_Delete_View.as_view(), name='Detail/Mod/Delete')
]
