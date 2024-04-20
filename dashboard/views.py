from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main import models
from .func import staff_required
from django.contrib import messages

# from django.db.models import Q


@staff_required
def index(request):
    staffs  = models.Staff.objects.all()
    
    context = {
        'staffs': staffs,
        
    }
    return render(request, 'index.html', context)



@staff_required
def staff_create(request):
    '''Bu yerda Staff yaratish uchun funksiya yozilgan'''
    if request.method == "POST":
        try:
            f_name = request.POST['f_name']
            l_name = request.POST['l_name']
            status = request.POST['status']
            tel_num = request.POST['tel_num']
            email = request.POST['email']

            models.Staff.objects.create(
                f_name = f_name,
                l_name = l_name,
                status = status,
                tel_num = tel_num,
                email = email
                )
            messages.success(request, 'categoriya created succesfully')
        except:
            messages.error(request, 'Something getting wrong')
    return render(request, 'staff/create.html')



@staff_required
def staff_list(request):
    '''Bu yerda stafflarning ro'yxatini ko'rish uchun funksiya yozilgan'''
    staff = models.Staff.objects.all()
    if request.method == 'POST':
        filter_items = {}
        for key,value in request.GET.items():
            if value:
                if key == 'start_date':
                    key = ''
        print(request.POST)

    context = {'staffs':staff}
    return render(request, 'staff/list.html', context)




@staff_required
def staff_detail(request, id):
    staff = models.Staff.objects.get(id=id)
    context = {'staff':staff}
    return render(request, 'staff/detail.html', context)




@staff_required
def staff_edit(request, id):
    staff = models.Staff.objects.get(id=id)
    if request.method == 'POST':
        try:
            staff.f_name = request.POST['f_name']
            staff.l_name = request.POST['l_name']
            staff.status = request.POST['status']
            staff.tel_num = request.POST['tel_num']
            staff.email = request.POST['email']
            staff.save()
            messages.success(request, "Xodim ma'limotlari movoffaqiyatli o'zgartirildi")
        except Exception as e:
            messages.error(request, f"Tahrirlashda xatolik yuz berdi: {e}")
        return redirect('staff_detail', id=id)
    context = {'staff': staff}
    return render(request, 'staff/edit.html', context)



def staff_delete(request, id):
    try:
        models.Staff.objects.get(id=id).delete()
        messages.error(request, 'Staff deleted')
    except:
        messages.error(request, 'Something getting wrong')
    return redirect('staff_list')


@staff_required
def profile(request):
    staffs = models.Staff.objects.all().count()
    users = User.objects.all().count()
    context = {
        'staffs': staffs,
        'users': users,
    }
    return render(request, 'profile/profile.html', context=context)


@staff_required
def settings(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')
    return render(request, 'profile/setting.html')
    


@staff_required
def product_list(request):
    staff = models.Staff.objects.all()
    staff_code = request.GET.get('staff_code')
    if staff_code:
        filter_items = {}
        for key, value in request.GET.items():
            if value and not value == '0':
                if key == 'start_date':
                    key = 'date__gte'
                elif key == 'end_date':    
                    key = 'date__lte'
                elif key == 'f_name':
                    key = 'staff__f_name__icontains'
                filter_items[key] = value

        enter = models.EnterStaff.objects.filter(**filter_items)

        print(enter)
        print(filter_items)

    queryset = models.Staff.objects.all()

    context = {
          'staff':staff,
          'staff_code':staff_code,
    }
    return render(request, 'staff/list.html', context)




def settings(request):

    return render(request, 'profile/setting.html')











def log_in(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            messages.success(request, 'Xush kelibsiz!')
        except:
            messages.error(request, 'Xatolik yuzberdi')
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'auth/login.html', {'error_message': 'Xatolik username yoki password.'})
    else:
        return render(request, 'auth/login.html')
    



def log_out(request):
    logout(request)
    redirect('logout')
    return render(request,'auth/logout.html')




# def query(request):
#     q = request.GET['q']
#     staff = models.Staff.objects.filter(Q(f_name=q) | Q(l_name=q) | Q(status=q) | Q(tel_num=q) | Q(email=q))
#     context = {
#         'staff':staff,
        
#     }
#     return render(request, 'query.html', context)



