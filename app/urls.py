from django.urls import path
from . import views

urlpatterns = [
    path('category-list/', views.CategoryAPIView.as_view()),
    path('product-list/', views.ProductAPIView.as_view()),
    path('category-product-list/', views.CategoryProductMixedAPIView.as_view()),
    path('new-list/', views.NewAPIWView.as_view()),
    path('faq-list/', views.FAQAPIView.as_view())

]