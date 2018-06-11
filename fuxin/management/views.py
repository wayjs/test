from django.shortcuts import render, redirect ,HttpResponse
from django import forms
from management import models
from management.pager import Pagination
import os
import json


# Create your views here.


def login(request):
    """
    用于登陆验证
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        n = request.POST.get("username")
        p = request.POST.get("pwd")
        obj = models.Consumer.objects.filter(username=n)
        if obj.count() == 0:
            return render(request, "login.html", {"error_user": "用户不存在"})
        elif obj.first().user_password == p:
            request.session["username"] = n
            request.session["is_login"] = True
            request.session.set_expiry(0)  # 设置超时时间 ,关闭浏览器，session 删除
            current_page = request.GET.get('p')
            my_count = models.Seed.objects.all().count()
            page_obj = Pagination(my_count, current_page, "/user")
            data_list = models.Seed.objects.all()[page_obj.start():page_obj.end()]
            return render(request, 'seed.html',{'data': data_list, 'page_obj': page_obj, "username": request.session.get("username")})

        else:
            return render(request, "login.html", {"error_pwd": "密码错误"})


def home(request):
    if request.session.get("is_login"):
        print(request.session.get("username"))
        return render(request, "home.html", {"username": request.session.get("username")})
    else:
        return render(request, "login.html")


def user(request):
    if request.session.get("is_login"):
        current_page = request.GET.get('p')
        my_count = models.Consumer.objects.all().count()
        page_obj = Pagination(my_count, current_page, "/user")
        data_list = models.Consumer.objects.all()[page_obj.start():page_obj.end()]
        return render(request, 'user.html', {'data': data_list, 'page_obj': page_obj,"username": request.session.get("username")})
    else:
        return render(request, "login.html")


def useradd(request):
    if request.session.get("is_login"):
        if request.method == "GET":
            return render(request, "useradd.html",{"username": request.session.get("username")})
        elif request.method == "POST":
            u = request.POST.get("addusername")
            pwd = request.POST.get("mypassword")
            role = request.POST.get("role")
            my_phone = request.POST.get("myphone")
            models.Consumer.objects.create(username=u, user_password=pwd, user_phone=my_phone, user_type=role)
            return redirect("/user/")
    else:
        return render(request, "login.html")


def usermodify(request, nid):
    if request.session.get("is_login"):
        user_info = models.Consumer.objects.filter(id=nid).first()
        return render(request, 'usermodify.html', {'user_info': user_info,"username": request.session.get("username")})
    else:
        return render(request, "login.html")

def seedmodify(request, nid):
    if request.session.get("is_login"):
        user_info = models.Seed.objects.filter(id = nid).first()
        return render(request,"seedmodify.html",{'user_info': user_info,"username": request.session.get("username")})
    else:
        return render(request, "login.html")

def modifyuser(request):
    if request.session.get("is_login"):
        u_id = request.POST.get("user_id")
        pwd = request.POST.get("mypassword")
        role = request.POST.get("role")
        my_phone = request.POST.get("myphone")
        models.Consumer.objects.filter(id=u_id).update(user_password=pwd, user_phone=my_phone, user_type=role)
        return redirect("/user/")
    else:
        return render(request, "login.html")

def modifyseed(request):
    if request.session.get("is_login"):
        u_id = request.POST.get("user_id")
        seed_num = request.POST.get("seed_num")
        seed_name = request.POST.get("seed_name")
        ke_name = request.POST.get("ke_name")
        shu_name = request.POST.get("shu_name")
        ya_name = request.POST.get("ya_name")
        character = request.POST.get("character")
        main_use = request.POST.get("main_use")
        climate = request.POST.get("climate")
        live = request.POST.get("live")
        flower = request.POST.get("flower")
        feature = request.POST.get("feature")
        seed_use = request.POST.get("seed_use")
        watch_place = request.POST.get("watch_place")
        breed = request.POST.get("breed")
        grow_year = request.POST.get("grow_year")
        save_year = request.POST.get("save_year")
        altitude = request.POST.get("altitude")
        podu = request.POST.get("podu")
        poxiang = request.POST.get("poxiang")
        soil_type = request.POST.get("soil_type")
        gps_x = request.POST.get("gps_x")
        gps_y = request.POST.get("gps_y")
        img_file = request.FILES.getlist("image")
        my_count = 0
        date_num = models.Seed.objects.all().last().id + 1
        print(date_num)
        photo_list = []
        for f in img_file:
            my_count += 1
            fname = "%s_%s.%s" % (date_num, my_count, f.name.split(".")[1])
            print(fname)
            destination = open(os.path.join("static/" + fname), 'wb')
            photo_list.append(os.path.join("/static/" + fname))
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        json_date = json.dumps(photo_list)
        models.Seed.objects.filter(id=u_id).update(seed_num=seed_num, seed_name=seed_name, ke_name=ke_name, shu_name=shu_name,
                                   ya_name=ya_name,
                                   character=character,
                                   main_use=main_use,
                                   climate=climate,
                                   live=live,
                                   flower=flower,
                                   feature=feature,
                                   seed_use=seed_use,
                                   watch_place=watch_place,
                                   breed=breed,
                                   grow_year=grow_year,
                                   save_year=save_year,
                                   altitude=altitude,
                                   podu=podu,
                                   poxiang=poxiang,
                                   soil_type=soil_type,
                                   gps_x=gps_x,
                                   gps_y=gps_y,
                                   status=0,
                                   seed_image=json_date
                                   )
        return redirect("/seed/")
    else:
        return render(request, "login.html")


def detailuser(request, nid):
    if request.session.get("is_login"):
        models.Consumer.objects.filter(id=nid).delete()
        return redirect("/user/")
    else:
        return render(request, "login.html")


def detailseed(request, nid):
    if request.session.get("is_login"):
        models.Seed.objects.filter(id=nid).delete()
        return redirect("/seed/")
    else:
        return render(request, "login.html")

def seed(request):
    if request.session.get("is_login"):
        current_page = request.GET.get('p')
        my_count = models.Seed.objects.all().count()
        page_obj = Pagination(my_count, current_page, "/user")
        data_list = models.Seed.objects.all()[page_obj.start():page_obj.end()]
        return render(request, 'seed.html', {'data': data_list, 'page_obj': page_obj,"username": request.session.get("username")})
    else:
        return render(request, "login.html")


def addseed(request):
    if request.session.get("is_login"):
        if request.method == "GET":
            return render(request, "addseed.html",{"username": request.session.get("username")})
        elif request.method == "POST":
            seed_num = request.POST.get("seed_num")
            seed_name = request.POST.get("seed_name")
            ke_name = request.POST.get("ke_name")
            shu_name = request.POST.get("shu_name")
            ya_name = request.POST.get("ya_name")
            character = request.POST.get("character")
            main_use = request.POST.get("main_use")
            climate = request.POST.get("climate")
            live = request.POST.get("live")
            flower = request.POST.get("flower")
            feature = request.POST.get("feature")
            seed_use = request.POST.get("seed_use")
            watch_place = request.POST.get("watch_place")
            breed = request.POST.get("breed")
            grow_year = request.POST.get("grow_year")
            save_year = request.POST.get("save_year")
            altitude = request.POST.get("altitude")
            podu = request.POST.get("podu")
            poxiang = request.POST.get("poxiang")
            soil_type = request.POST.get("soil_type")
            gps_x = request.POST.get("gps_x")
            gps_y = request.POST.get("gps_y")
            img_file = request.FILES.getlist("image")
            my_count = 0
            date_num = models.Seed.objects.all().last().id + 1
            print(date_num)
            photo_list = []
            for f in img_file:
                my_count += 1
                fname = "%s_%s.%s" % (date_num, my_count, f.name.split(".")[1])
                print(fname)
                destination = open(os.path.join("static/" + fname), 'wb')
                photo_list.append(os.path.join("/static/" + fname))
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
            json_date = json.dumps(photo_list)
            models.Seed.objects.create(seed_num=seed_num,seed_name=seed_name,ke_name=ke_name,shu_name=shu_name,ya_name=ya_name,
                character=character,
                main_use=main_use,
                climate=climate,
                live=live,
                flower=flower,
                feature=feature,
                seed_use=seed_use,
                watch_place=watch_place,
                breed=breed,
                grow_year=grow_year,
                save_year=save_year,
                altitude=altitude,
                podu=podu,
                poxiang=poxiang,
                soil_type=soil_type,
                gps_x=gps_x,
                gps_y=gps_y,
                status=0,
                seed_image=json_date
            )
            return render(request,"addseed.html",{"username": request.session.get("username")})
    else:
        return render(request, "login.html")


def searchseed(request):
    if request.session.get("is_login"):
        find_type = request.POST.get("search_select")
        find_seed = request.POST.get("seed_select")
        if find_type == "1":
            current_page = request.GET.get('p')
            my_count = models.Seed.objects.filter(seed_name__icontains=find_seed).count()
            page_obj = Pagination(my_count, current_page, "/user")
            data_list = models.Seed.objects.filter(seed_name__icontains=find_seed)[page_obj.start():page_obj.end()]
            return render(request, 'seed.html', {'data': data_list, 'page_obj': page_obj,"username": request.session.get("username")})
        elif find_type == "2":
            current_page = request.GET.get('p')
            my_count = models.Seed.objects.filter(ya_name__icontains=find_seed).count()
            page_obj = Pagination(my_count, current_page, "/user")
            data_list = models.Seed.objects.filter(ya_name__icontains=find_seed)[page_obj.start():page_obj.end()]
            return render(request, 'seed.html', {'data': data_list, 'page_obj': page_obj,"username": request.session.get("username")})
        elif find_type == "3":
            current_page = request.GET.get('p')
            my_count = models.Seed.objects.filter(seed_use__icontains=find_seed).count()
            page_obj = Pagination(my_count, current_page, "/user")
            data_list = models.Seed.objects.filter(seed_use__icontains=find_seed)[page_obj.start():page_obj.end()]
            return render(request, 'seed.html', {'data': data_list, 'page_obj': page_obj,"username": request.session.get("username")})
    else:
        return render(request, "login.html")


def auditer(request):
    if request.session.get("is_login"):
        current_page = request.GET.get('p')
        my_count = models.Seed.objects.filter(status="0").count()
        page_obj = Pagination(my_count, current_page, "/user")
        data_list =models.Seed.objects.filter(status="0")[page_obj.start():page_obj.end()]
        return render(request, 'auditer.html', {'data': data_list, 'page_obj': page_obj,"username": request.session.get("username")})
    else:
        return render(request, "login.html")


def auditerss(request,nid):
    if request.session.get("is_login"):
        user_info = models.Seed.objects.filter(id=nid).first()
        obj = models.Seed.objects.filter(id=nid)
        for i in obj:
            my_data = i.seed_image
        obj = json.loads(my_data)
        return render(request, "seeddetail.html", {'user_info': user_info,"obj": obj,"username": request.session.get("username")})
    else:
        return render(request, "login.html")


def status(request):
    if request.session.get("is_login"):
        nid = request.POST.get("user_id")
        models.Seed.objects.filter(id=nid).update(status="1", auditor=request.session.get("username"))
        return redirect("/auditer/")
    else:
        return render(request, "login.html")

