from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Expense
from django.views.decorators.csrf import csrf_exempt
from .models import Goal
import yfinance as yf
import requests
from .models import Question, Answer, QuizResult

# home view
def home(request):
    return render(request, 'Finsavvy/home.html')

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = UserRegisterForm()
    return render(request, 'Finsavvy/register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            User = get_user_model()  # Get the user model

            # Attempt to authenticate with either username or email
            if email:
                try:
                    user = User.objects.get(email=email)  # Get user by email
                    user = authenticate(request, username=user.username, password=password)  # Authenticate using username
                except User.DoesNotExist:
                    user = None  # If no user found, set to None
            elif username:
                user = authenticate(request, username=username, password=password)  # Authenticate using username

            # Check if the user is authenticated
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}. You are now logged in.")
                return redirect('dashboard')
            else:
                messages.error(request, 'Login failed. Please check your email/username and password.')
        else:
            messages.error(request, 'Invalid login credentials.')
    else:
        form = UserLoginForm()
    return render(request, 'Finsavvy/login.html', {'form': form})


# dashboard view
def dashboard(request):
     if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to view this page.")
        return redirect('login')
     return render(request, 'Finsavvy/dashboard.html')

# learning modules
@login_required
def learning_modules(request):
    return render(request, 'Finsavvy/learning_modules.html')

@login_required
def personalized_budget_planner(request):
    return render(request, 'Finsavvy/personalized_budget_planner.html')

@login_required
def goal_setting_tracking(request):
    return render(request, 'Finsavvy/goal_setting_tracking.html')

@login_required
def progress_quizzes(request):
    return render(request, 'Finsavvy/progress_quizzes.html')
# logout view
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')

# New views for each module
def module_1(request):
    return render(request, 'Finsavvy/learning_modules/budgeting_basics.html')

def module_2(request):
    return render(request, 'Finsavvy/learning_modules/understanding_debt.html')

def module_3(request):
    return render(request, 'Finsavvy/learning_modules/smart_saving_strategies.html')

def module_4(request):
    return render(request, 'Finsavvy/learning_modules/introduction_to_investments.html')

def module_5(request):
    return render(request, 'Finsavvy/learning_modules/retirement_savings_strategies.html')

def module_6(request):
    return render(request, 'Finsavvy/learning_modules/financial_planning_goal_setting.html')

def module_7(request):
    return render(request, 'Finsavvy/learning_modules/managing_financial_risks.html')

def module_8(request):
    return render(request, 'Finsavvy/learning_modules/taxes_and_tax_planning.html')

def module_9(request):
    return render(request, 'Finsavvy/learning_modules/building_wealth_over_time.html')

def module_10(request):
    return render(request, 'Finsavvy/learning_modules/creating_an_emergency_fund.html')

def personalized_budget_planner(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'Finsavvy/personalized_budget_planner.html', {'expenses': expenses})

@csrf_exempt
def add_expense(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        expense = Expense.objects.create(user=request.user, category=category, amount=amount)
        return JsonResponse({'success': True, 'expense_id': expense.id})

    return JsonResponse({'success': False}, status=400)

@login_required
def goal_setting_tracking(request):
    if request.method == 'POST':
        goal_name = request.POST['goal_name']
        goal_amount = request.POST['goal_amount']
        goal_deadline = request.POST['goal_deadline']

        Goal.objects.create(
            user=request.user,
            name=goal_name,
            amount=goal_amount,
            deadline=goal_deadline
        )
        return redirect('goal_setting_tracking')

    goals = Goal.objects.filter(user=request.user)
    return render(request, 'Finsavvy/goal_setting_tracking.html', {'goals': goals})

@login_required
def real_time_financial_tips(request):
    tips = get_external_tips()  # Fetch the financial tips
    return render(request, 'Finsavvy/real_time_financial_tips.html', {'tips': tips})

def get_external_tips():
    """Fetch financial data for a particular stock"""
    stock = yf.Ticker("AAPL")  # You can change this ticker to any other stock
    stock_info = stock.info
    stock_price = stock_info.get('regularMarketPrice')
    
    # Custom financial tip based on stock price
    tip = f"Apple stock price is ${stock_price}. It may be a good time to invest."
    
    return [{"title": "Stock Market Update", "content": tip}]

def api_financial_tips(request):
    """API endpoint for real-time financial tips"""
    external_tips = get_external_tips()
    return JsonResponse({"tips": external_tips})

def api_notifications(request):
    """API endpoint for user notifications"""
    notifications = [
        {"message": "You have a new financial recommendation!", "created_at": "2024-10-01"}
    ]
    return JsonResponse({"notifications": notifications})


@login_required
def progress_quizzes(request):
    if request.method == "POST":
        score = 0
        total_questions = Question.objects.count()

        for question in Question.objects.all():
            selected_answer_id = request.POST.get(f'question_{question.id}')
            if selected_answer_id:
                selected_answer = Answer.objects.get(id=selected_answer_id)
                if selected_answer.is_correct:
                    score += 1

        # Save the user's result
        QuizResult.objects.create(user=request.user, score=score)

        # Redirect to results page
        return redirect('quiz_results')

    questions = Question.objects.prefetch_related('answers').all()
    return render(request, 'Finsavvy/progress_quizzes.html', {'questions': questions})

@login_required
def quiz_results(request):
    user_scores = QuizResult.objects.filter(user=request.user).order_by('-date_taken')
    return render(request, 'Finsavvy/quiz_results.html', {'user_scores': user_scores})


