from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext, Context, Template
from django.core.mail import EmailMultiAlternatives
import datetime

# Create your views here.
from django.urls import reverse_lazy

from teacherManage.models import *


def index_student(request):
    pre_student = Student.objects.get(email=request.GET.get('email'))
    return render(request, 'index_student.html', {'pre_student': pre_student})


def index_teacher(request):
    pre_teacher = Teacher.objects.get(email=request.GET.get('email'))
    return render(request, 'index_teacher.html', {'pre_teacher': pre_teacher})


def all_teacher(request):
    pre_student = Student.objects.get(email=request.GET.get('email'))
    all_teachers = Teacher.objects.all()
    show_teachers = []
    for t in all_teachers:
        if t.tag:
            show_teachers.append(t)
    dic = {'show_teachers': show_teachers, 'pre_student': pre_student}
    return render(request, 'all_teacher.html', dic)


def all_teacher_tour(request):
    show_teachers = Teacher.objects.filter(tag=True)
    return render(request, 'all_teacher_tour.html', {'show_teachers': show_teachers})


def teacher_all_teacher(request):
    pre_teacher = Teacher.objects.get(email=request.GET.get('email'))
    all_teachers = Teacher.objects.all()
    show_teachers = []
    for t in all_teachers:
        if t.tag:
            show_teachers.append(t)
    dic = {'show_teachers': show_teachers, 'pre_teacher': pre_teacher}
    return render(request, 'teacher_all_teacher.html', dic)


def recommend_teacher(request):
    pre_student = Student.objects.get(email=request.GET.get('email'))
    recommend_teachers = []
    all_teachers = Teacher.objects.all()
    for t in all_teachers:
        if t.tag:
            if t.academy == pre_student.academy:
                recommend_teachers.append(t)
    dic = {'recommend_teachers': recommend_teachers, 'pre_student': pre_student}
    return render(request, 'recommend_teacher.html', dic)


def show(request):
    teachers = Teacher.objects.all()
    show_teachers = []
    for t in teachers:
        if t.tag:
            show_teachers.append(t)
    dic = {'show_teachers': show_teachers}
    return render(request, 'show.html', dic)


def search_teacher(request):
    students = Student.objects.all()
    if request.method == 'POST':
        pre_student_email = request.POST.get('email')
        for s in students:
            if s.email == pre_student_email:
                teacher_search_lst = Teacher.objects.filter(name=request.POST.get('search_name'))
                dic = {'teacher_search_lst': teacher_search_lst, 'pre_student': s}
                return render(request, 'searchTeacher.html', dic)


def tour_search(request):
    if request.method == 'POST':
        teacher_search_lst = Teacher.objects.filter(name=request.POST.get('search_name'))
        return render(request, 'tour_search.html', {'teacher_search_lst': teacher_search_lst})

def teacher_find(request):
    pre_teacher = Teacher.objects.get(email=request.POST.get('email'))
    if request.method == 'POST':
        teacher_search_lst = Teacher.objects.filter(name=request.POST.get('search_name'))
        dic = {'pre_teacher': pre_teacher, 'teacher_search_lst': teacher_search_lst}
        return render(request, 'teacher_search_teacher.html', dic)



def VIP_search(request):
    if request.method == 'POST':
        teacher_search_lst = Teacher.objects.filter(name=request.POST.get('search_name'))
        return render(request, 'VIP_search.html', {'teacher_search_lst': teacher_search_lst})


def show_teacher_details(request):
    show_teacher = Teacher.objects.get(pk=request.GET.get('pk'))
    pre_student = Student.objects.get(email=request.GET.get('email'))
    dic = {'show_teacher': show_teacher, 'pre_student': pre_student}
    return render(request, 'teacherinformation.html', dic)


def details_to_teacher(request):
    show_teacher = Teacher.objects.get(pk=request.GET.get('pk'))
    pre_teacher = Teacher.objects.get(email=request.GET.get('email'))
    dic = {'show_teacher': show_teacher, 'pre_teacher': pre_teacher}
    return render(request, 'teacherinformation_teacher.html', dic)

def details_to_tour(request):
    show_teacher = Teacher.objects.get(email=request.GET.get('email'))
    return render(request, 'details_to_tour.html', {'show_teacher': show_teacher})


def details_to_VIP(request):
    show_teacher = Teacher.objects.get(pk=request.GET.get('pk'))
    return render(request, 'details_to_VIP.html', {'show_teacher': show_teacher})


def teacher_information(request):
    show_teacher = Teacher.objects.get(pk=request.GET.get('pk'))
    pre_teacher = Teacher.objects.get(email=request.GET.get('email'))
    dic = {'show_teacher': show_teacher, 'pre_teacher': pre_teacher}
    return render(request, 'teacherinformation_teacher.html', dic)


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        userResult = Student.objects.filter(password=password, email=email)
        pre_student = Student.objects.get(email=email)
        if (len(userResult) > 0):
            return render(request, 'index_student.html', {'pre_student': pre_student})
        else:
            return render(request, 'error1.html')


def register(request):
    if request.method == 'POST':
        email1 = request.POST.get('email')
        newStudent = Student(
            name=request.POST.get('username'),
            password=request.POST.get('password'),
            email=request.POST.get('email'),
            tel=request.POST.get('phone'),
            education=request.POST.get('education'),
            academy=request.POST.get('academy'),
            hobby=request.POST.get('hobby'),
        )
        filterResult = Student.objects.filter(email=email1)
        if len(filterResult) > 0:
            return render(request, 'error.html')
        else:
            newStudent.save()
            return render(request, 'success.html')


def register_teacher(request):
    if request.method == 'POST':
        email1 = request.POST.get('email')
        newTeacher = Teacher(
            name=request.POST.get('username'),
            password=request.POST.get('password'),
            email=request.POST.get('email'),
            tel=request.POST.get('phone'),
            academy=request.POST.get('academy'),
            sex=request.POST.get('radio')
        )
        filterResult = Teacher.objects.filter(email=email1)
        if len(filterResult) > 0:
            return render(request, 'error_teacher.html')
        else:
            newTeacher.save()
            return render(request, 'success_teacher.html')


def login_teacher(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        userResult = Teacher.objects.filter(password=password, email=email)
        pre_teacher = Teacher.objects.get(email=email)
        if (len(userResult) > 0):
            # return render(request,'teacher.html')
            return render(request, 'index_teacher.html', {'pre_teacher': pre_teacher})
        else:
            return render(request, 'error1_teacher.html')


def login_VIP(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        userResult = VIP.objects.filter(password=password, email=email)
        if (len(userResult) > 0):
            return show_to_vip(request)
        else:
            return render(request, 'error_VIP.html')


def register_choice(request):
    return render(request, 'register_choice.html')


def login1(request):
    return render(request, 'login.html')


def register1(request):
    return render(request, 'register.html')


def login2(request):
    return render(request, 'login_teacher.html')


def register2(request):
    return render(request, 'register_teacher.html')


def login3(request):
    return render(request, 'VIP_login.html')


def tour(request):
    return render(request, 'show.html')


def make_appointment(request):
    the_student = Student.objects.get(email=request.GET.get('student_email'))
    the_teacher = Teacher.objects.get(email=request.GET.get('teacher_email'))
    new_appointment = Appointment(
        student=the_student.name,
        teacher=the_teacher.name,
        student_email=the_student.email,
        teacher_email=the_teacher.email,
        date=datetime.date.today(),
        time=1,
    )
    new_appointment.save()
    pre_student = Student.objects.get(email=new_appointment.student_email)
    dic = {'the_student': the_student, 'the_teacher': the_teacher, 'new_appointment': new_appointment, 'pre_student': pre_student}

    return render(request, 'order.html', dic)


def submit_appointment(request):
    if request.method == 'POST':
        pre_topic = request.POST.get('topic')
        pre_pk = int(request.POST.get('pre_pk'))
        the_appointment = Appointment.objects.get(pk=pre_pk)
        pre_student = Student.objects.get(email=the_appointment.student_email)
        if pre_topic:
            the_appointment.date = request.POST.get('date')
            the_appointment.time = request.POST.get('time')
            the_appointment.topic = pre_topic
            the_appointment.content = request.POST.get('content')
            the_appointment.save()
            return render(request, 'success_date.html', {'pre_student': pre_student})
        else:
            the_appointment.delete()
        return render(request, 'all_teacher.html')


def rule_appointments(request):
    return render(request, 'rule_appointments.html')


def teacher(request, email):
    pre_teacher = Teacher.objects.get(email=email)
    teachers = Teacher.objects.all()
    dic = {'teachers': teachers, 'pre_teacher': pre_teacher}

    return render(request, 'teacher.html', dic)


def show_to_student(request, email):
    pre_student = Student.objects.get(email=email)
    teachers = Teacher.objects.all()

    recommend_teacher = []
    for a in teachers:
        if pre_student.academy == a.academy:
            recommend_teacher.append(a)

    dic = {'teachers': teachers, 'recommend_teacher': recommend_teacher, 'pre_student': pre_student}

    return render(request, 'show_to_student.html', dic)


update_teacher_pk = -1


def teacher_update(request):
    the_teacher = Teacher.objects.get(email=request.GET.get('email'))
    global update_teacher_pk
    update_teacher_pk = the_teacher.pk
    return render(request, 'teacher_update.html', {'the_teacher': the_teacher})


def update_details(request):
    global update_teacher_pk
    if request.method == 'POST':
        pre_teacher_email = request.POST.get('email')
        teachers = Teacher.objects.all()
        for t in teachers:
            if t.email == pre_teacher_email:
                t.age = request.POST.get('age')
                t.tel = request.POST.get('tel')
                t.address = request.POST.get('address')
                t.title = request.POST.get('title')
                t.research = request.POST.get('research')
                t.tag = False
                t.save()
                break
        return render(request, 'change_information_hint.html', {'pre_teacher': t})


def teacher_change_information(request):
    pre_teacher = Teacher.objects.get(email=request.GET.get('email'))
    return render(request, 'teacher_change_information.html', {'pre_teacher': pre_teacher})



def show_to_vip(request):
    teachers = Teacher.objects.all()
    dic = {'teachers': teachers}
    return render(request, 'VIP.html', dic)


def show_to_tour(request):
    return render(request, 'show_to_tour.html')


def allow_teacher(request, pk):
    allow_t = Teacher.objects.get(pk=pk)
    allow_t.tag = True
    allow_t.save()
    teachers = Teacher.objects.all()
    return render(request, 'VIP.html', {'teachers': teachers})


def found_student(request):
    if request.method == 'POST':
        email1 = request.POST.get('email')
        student_serach = Student.objects.all()
        for S in student_serach:
            if S.email == email1:
                password_result = S.password
                subject, form_email, to = 'Result', '1078161458@qq.com', email1
                text_content = password_result
                msg = EmailMultiAlternatives(subject, text_content, form_email, [to])
                msg.send()
                return render(request, 'success_password_found.html')
        return render(request, 'error_password_found.html')


def found_teacher(request):
    if request.method == 'POST':
        email1 = request.POST.get('email')
        teacher_serach = Teacher.objects.all()
        for S in teacher_serach:
            if S.email == email1:
                password_result = S.password
                subject, form_email, to = 'Result', '1078161458@qq.com', email1
                text_content = password_result
                msg = EmailMultiAlternatives(subject, text_content, form_email, [to])
                msg.send()
                return render(request, 'success_password_found.html')
            else:
                return render(request, 'error_password_found.html')


def found_password_choice(request):
    return render(request, 'found_password_choice.html')


def found_student1(request):
    return render(request, 'found_student.html')


def found_teacher1(request):
    return render(request, 'found_teacher.html')


def change_password(request):
    pre_student = Student.objects.get(email=request.GET.get('email'))
    return render(request, 'change_password.html', {'pre_student': pre_student})


def password_change(request):
    if request.method == "POST":
        email1 = request.POST.get('email')
        pre_student = Student.objects.get(email=email1)
        password1 = request.POST.get('old_password')
        password2 = request.POST.get('new_password')
        student_serach = Student.objects.all()
        for S in student_serach:
            if S.email == email1:
                if S.password == password1:
                    S.password = password2
                    S.save()
                    return render(request, 'success_password_change.html', {'pre_student': pre_student})
                else:
                    return render(request, 'error_password_change.html', {'pre_student': pre_student})


def teacher_change_password(request):
    pre_teacher = Teacher.objects.get(email=request.GET.get('email'))
    return render(request, 'teacher_change_password.html', {'pre_teacher': pre_teacher})


def password_change_teacher(request):
    if request.method == "POST":
        email1 = request.POST.get('email')
        pre_teacher = Teacher.objects.get(email=email1)
        password1 = request.POST.get('old_password')
        password2 = request.POST.get('new_password')
        teacher_serach = Teacher.objects.all()
        for S in teacher_serach:
            if S.email == email1:
                if S.password == password1:
                    S.password = password2
                    S.save()
                    return render(request, 'teacher_update_pwd.html', {'pre_teacher': pre_teacher})
                else:
                    return render(request, 'teacher_update_pwd_wrong.html', {'pre_teacher': pre_teacher})


def look_date(request):
    flag = False
    appointments = Appointment.objects.all()
    pre_student = Student.objects.get(email=request.GET.get('email'))
    pre_student_appointments = []
    for a in appointments:
        if a.topic:
            if a.student_email == pre_student.email:
                pre_student_appointments.append(a)
                flag = True
        else:
            a.delete()
    dic = {'pre_student': pre_student, 'pre_student_appointments': pre_student_appointments}
    if flag:
        return render(request, 'look_date.html', dic)
    else:
        return render(request, 'none_order.html', dic)


def look_date_teacher(request):
    flag = False
    pre_teacher = Teacher.objects.get(email=request.GET.get('email'))
    appointments = Appointment.objects.all()
    pre_teacher_appointments = []
    for a in appointments:
        if a.teacher == pre_teacher.name:
            pre_teacher_appointments.append(a)
            flag = True
    dic = {'pre_teacher_appointments': pre_teacher_appointments, 'pre_teacher': pre_teacher}
    if flag:
        return render(request, 'look_date_teacher.html', dic)
    else:
        return render(request, 'none_order_teacher.html', dic)


def allow_appointment(request):
    the_appointment = Appointment.objects.get(pk=request.GET.get('pk'))
    the_appointment.tag = 1
    the_appointment.save()
    return look_date_teacher(request)


def refuse_appointment(request):
    the_appointment = Appointment.objects.get(pk=request.GET.get('pk'))
    the_appointment.tag = 0
    the_appointment.save()
    return look_date_teacher(request)
