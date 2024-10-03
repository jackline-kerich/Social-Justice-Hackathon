from django.urls import path, include
from . import views
from .views import personalized_budget_planner, add_expense

urlpatterns = [
    path('', views.home, name='home'), 
    path('register/', views.register, name='register'),  
    path('login/', views.user_login, name='login'),  
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('learning-modules/', views.learning_modules, name='learning_modules'),  
    path('personalized-budget-planner/', views.personalized_budget_planner, name='personalized_budget_planner'),  # New
    path('add-expense/', add_expense, name='add_expense'),  # New
    path('goal-setting-tracking/', views.goal_setting_tracking, name='goal_setting_tracking'),  # New
    path('real-time-financial-tips/', views.real_time_financial_tips, name='real_time_financial_tips'),  # New
    path('api/financial-tips/', views.api_financial_tips, name='api_financial_tips'),
    path('api/notifications/', views.api_notifications, name='api_notifications'),
    path('progress-quizzes/', views.progress_quizzes, name='progress_quizzes'), 
    path('quiz_results/', views.quiz_results, name='quiz_results'), 
    path('logout/', views.user_logout, name='logout'),  
     # New paths for each module
    path('module-1/', views.module_1, name='module_1'),  
    path('module-2/', views.module_2, name='module_2'),  
    path('module-3/', views.module_3, name='module_3'),  
    path('module-4/', views.module_4, name='module_4'),  
    path('module-5/', views.module_5, name='module_5'),  
    path('module-6/', views.module_6, name='module_6'),  
    path('module-7/', views.module_7, name='module_7'),  
    path('module-8/', views.module_8, name='module_8'),  
    path('module-9/', views.module_9, name='module_9'),  
    path('module-10/', views.module_10, name='module_10'), 
]
