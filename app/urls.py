from django.urls import path
from . import views
from drf_spectacular.views  import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('category-list/', views.CategoryAPIView.as_view()),
    path('product-list/', views.ProductAPIView.as_view()),
    path('category-product-list/', views.CategoryProductMixedAPIView.as_view()),
    path('new-list/', views.NewAPIWView.as_view()),
    path('about-us-list/', views.AboutUsAPIView.as_view()),
    path('user-email-create/', views.UserEmailAPIView.as_view()),
    path('feedback-list/', views.FeedbackAPIView.as_view()),
    path('faq-list/', views.FAQAPIView.as_view()),
    path('app-object/', views.ApplicationObjectCreateAPIView.as_view()),
    path('branch-list/', views.BranchAPIView.as_view()),
    path('user-create/', views.UserCreateAPIView.as_view()),
    path('user-location-list/', views.UserLocationAPIView.as_view()),
    path('user-card-list/', views.UserCardAPIView.as_view()),
    path('vacancy-application-create/', views.VacancyApplicationAPIView.as_view()),
    path('vacancy-application-list/', views.VacancyVacancyApplicationMixedAPIView.as_view()),
    path('career-list/', views.CareerAPIView.as_view()),
    path('order-product-list/', views.OrderOrderProductMixedAPIView.as_view()),
    path('certificate-list/', views.CertificateAPIView.as_view()),
    

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]