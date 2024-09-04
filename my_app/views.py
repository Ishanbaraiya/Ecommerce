from django.shortcuts import render,redirect
from django.contrib import messages
from .models import*
import random
import requests
from django.core.mail import send_mail 
from django.core.paginator import Paginator
from django.utils import timezone
import razorpay

# Create your views here.
def index(request):
    if 'email' in request.session:
        uid=signup.objects.get(email=request.session['email'])
        mid = categories.objects.all()
        product = products.objects.all()
        get_color_category = color.objects.all()
        sort_order = request.GET.get('sort','name_asc')
        get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
        get_cart = add_to_cart.objects.filter(user_id=uid)
        get_wishlist_count = wish_list.objects.filter(user_id=uid).count()
        get_wishlist = wish_list.objects.filter(user_id = uid)
        get_wishlist1 = wish_list.objects.filter(user_id = uid).values_list('products_id',flat=True)

        if sort_order:
            if sort_order == 'name_asc':
                product = products.objects.order_by('name')
            elif sort_order == 'price_asc':
                product = products.objects.order_by('price')
            elif sort_order == 'price_desc':
                product = products.objects.order_by('-price')
            else:
                product = products.objects.order_by('-name')
        else:
            product = products.objects.all()

        contaxt={"uid" : uid, "mid" : mid, "product" : product,"get_color_category":get_color_category, "get_cart" : get_cart,
                 "get_cart_count":get_cart_count,"get_wishlist_count":get_wishlist_count,"get_wishlist":get_wishlist,"get_wishlist1":get_wishlist1}
        return render(request, "index.html",contaxt) 
    else:
        return render(request, "login.html") 

def search(request):
    uid = signup.objects.get(email=request.session['email'])
    get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
    get_wishlist = wish_list.objects.filter(user_id = uid)
    get_wishlist_count = wish_list.objects.filter(user_id=uid).count()

    product = products.objects.all()
    if request.POST:
        srh = request.POST['search']
        if srh:
            product = products.objects.filter(name__icontains=srh)
        contaxt = {"product": product,"get_cart_count": get_cart_count,
                   "get_wishlist_count": get_wishlist_count,"get_wishlist":get_wishlist} 
        return render(request,"index.html",contaxt)

def about(request):
    uid = signup.objects.get(email=request.session['email'])
    get_wishlist_count = wish_list.objects.filter(user_id=uid).count()
    get_wishlist = wish_list.objects.filter(user_id = uid)
    get_cart_count = add_to_cart.objects.filter(user_id=uid).count()

    get_cart = add_to_cart.objects.filter(user_id=uid)

    context = {"get_cart": get_cart, "get_cart_count": get_cart_count,
               "get_wishlist_count":get_wishlist_count, "get_wishlist":get_wishlist} 
    return render(request,"about.html",context)

def blog_detail(request):
    uid = signup.objects.get(email=request.session['email'])
    get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
    get_cart = add_to_cart.objects.filter(user_id=uid)
    get_wishlist_count = wish_list.objects.filter(user_id=uid).count()
    get_wishlist = wish_list.objects.filter(user_id = uid)

    context = {"get_cart": get_cart,"get_cart_count": get_cart_count,
               "get_wishlist_count":get_wishlist_count, "get_wishlist":get_wishlist} 
    return render(request, "blog_detail.html",context)

def blog(request):
    uid = signup.objects.get(email=request.session['email'])
    get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
    get_cart = add_to_cart.objects.filter(user_id=uid)
    get_wishlist_count = wish_list.objects.filter(user_id=uid).count()
    get_wishlist = wish_list.objects.filter(user_id = uid)

    context = {"get_cart": get_cart, "get_cart_count":get_cart_count,
               "get_wishlist_count":get_wishlist_count, "get_wishlist":get_wishlist} 
    return render(request, "blog.html",context)

def contact(request):
    uid = signup.objects.get(email=request.session['email'])
    get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
    get_cart = add_to_cart.objects.filter(user_id=uid)
    get_wishlist_count = wish_list.objects.filter(user_id=uid).count()
    get_wishlist = wish_list.objects.filter(user_id = uid)

    if request.POST:
        e_mail = request.POST['email']
        msg = request.POST['msg']
        contacts.objects.create(email=e_mail,msg=msg)
        return redirect("contact")
    context = {"get_cart": get_cart,"get_cart_count": get_cart_count,
               "get_wishlist_count":get_wishlist_count, "get_wishlist": get_wishlist} 
    return render(request, "contact.html",context)

def product_detail(request,id):
    uid = signup.objects.get(email=request.session['email'])
    get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
    get_cart = add_to_cart.objects.filter(user_id=uid)
    get_wishlist_count = wish_list.objects.filter(user_id=uid).count()
    get_wishlist = wish_list.objects.filter(user_id = uid)
    get_prodduct = products.objects.get(id=id)
    size = get_prodduct.size.all()
    color = get_prodduct.color.all()


    context = {"get_product" : get_prodduct, "uid" : uid,"get_cart": get_cart,"color": color,"size": size,
               "get_cart_count": get_cart_count,"get_wishlist_count":get_wishlist_count, "get_wishlist": get_wishlist}
    return render(request, "product_detail.html",context) 
    
def product(request):
    uid = signup.objects.get(email=request.session['email'])
    get_cart = add_to_cart.objects.filter(user_id=uid)
    get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
    get_wishlist = wish_list.objects.filter(user_id = uid)
    get_wishlist1 = wish_list.objects.filter(user_id = uid).values_list('products_id',flat=True)
    get_wishlist_count = wish_list.objects.filter(user_id=uid).count()
    get_color_category = color.objects.all()
    mid = categories.objects.all()
    product = products.objects.all()  
    sort_order = request.GET.get('sort','name_desc')

    if sort_order:
        if sort_order == 'name_asc':
            product = products.objects.order_by('name')
        elif sort_order == 'price_asc':
            product = products.objects.order_by('price')
        elif sort_order == 'price_desc':
            product = products.objects.order_by('-price')
        else:
            product = products.objects.order_by('-name')
    else:
            product = products.objects.all()

    paginator = Paginator(product,4)
    page_number = request.GET.get("page",1)
    product = paginator.get_page(page_number)
    show_page = paginator.get_elided_page_range(page_number,on_each_side=1,on_ends=1)

    context = {'mid' : mid , 'product' : product, "get_color_category":get_color_category,"show_page":show_page,
               "get_cart": get_cart,"get_cart_count":get_cart_count,"get_wishlist_count":get_wishlist_count,"get_wishlist":get_wishlist,"get_wishlist1":get_wishlist1}
    return render(request, "product.html", context)

def price_filter(request):
    if 'email' in request.session:
        uid = signup.objects.get(email=request.session['email'])
        get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
        get_cart = add_to_cart.objects.filter(user_id=uid)
        get_wishlist_count = wish_list.objects.filter(user_id=uid).count()
        get_wishlist = wish_list.objects.filter(user_id = uid)
        get_categories = categories.objects.all()
        get_color_category = color.objects.all()
        get_color = color.objects.all()
        get_products = products.objects.all()
        min_price = request.GET.get("min")
        max_price = request.GET.get("max")

        if not min_price and not max_price:
            return redirect("product")
        else:
            try:
                get_products = products.objects.filter(price__gte = min_price, price__lte = max_price) 
            except ValueError:
                return redirect("product")
        
            contaxt = {"get_products": get_products, "get_categories": get_categories, "get_color": get_color,
                       "get_cart_count":get_cart_count,"get_color_category":get_color_category,"get_wishlist_count":get_wishlist_count,
                       "get_wishlist":get_wishlist,"get_cart":get_cart} 
            return render(request, "product.html", contaxt)
    else:
        return render(request, "login.html")
    
def color_filter(request):
    if 'email' in request.session:
        uid = signup.objects.get(email=request.session['email'])
        get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
        get_cart = add_to_cart.objects.filter(user_id=uid)
        get_wishlist_count = wish_list.objects.filter(user_id=uid).count()
        get_wishlist = wish_list.objects.filter(user_id = uid)
        get_categories = categories.objects.all()
        get_products = products.objects.all()
        get_color_category = color.objects.all()
        product_color = request.GET.getlist("get_color_name")
        get_products = []


        if product_color == []:
            return redirect("product")
        else:
            for i in product_color:
                get_color_name = color.objects.get(name=i)
                set_product_color_wise = products.objects.filter(color_id=get_color_name)
                get_products.extend(set_product_color_wise)
                contaxt = {"get_products": get_products,"get_categories": get_categories,"get_color_category":get_color_category,
                       "get_cart_count":get_cart_count,"get_wishlist_count":get_wishlist_count,"get_wishlist":get_wishlist,"get_cart":get_cart}  
            return render(request, "product.html", contaxt)
    else:
        return render(request, "login.html")

def add_cart(request,id):
    if 'email' in request.session:
        uid = signup.objects.get(email=request.session['email'])
        get_product = products.objects.get(id=id)
        cart_id = add_to_cart.objects.filter(products_id=get_product,user_id=uid)
        
        if cart_id:
            get_cart = add_to_cart.objects.get(products_id=get_product,user_id=uid)
            if request.POST:
                size = request.POST['size']
                color = request.POST['color']
                if get_cart.size and get_cart.color:
                    get_cart.size = size
                    get_cart.color = color
            get_cart.quantity = get_cart.quantity + 1           
            get_cart.total_prize = get_cart.quantity * get_product.price
            
            get_cart.save()
            
        else:
            add_to_cart.objects.create(products_id=get_product,user_id=uid,name=get_product.name,total_prize=get_product.price,quantity=1,img=get_product.img,price=get_product.price)
        return redirect("shoping_cart")
    else:
        return render(request,"login.html")
   
def shoping_cart(request):
    if 'email' in request.session:
        uid = signup.objects.get(email=request.session['email'])
        get_cart  = add_to_cart.objects.filter(user_id=uid)
        get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
        get_wishlist_count = wish_list.objects.filter(user_id=uid).count()
        get_wishlist = wish_list.objects.filter(user_id = uid)
        all_product = []
        dilivery_chag = 100
        discount = 0
        total_amount = 0

        for i in get_cart:
            all_product.append(i.total_prize)
        get_subtotal = sum(all_product)
        total_amount = get_subtotal + dilivery_chag + discount
        context = {"get_cart":get_cart,"get_cart_count":get_cart_count,"get_subtotal":get_subtotal, "discount": discount,
                   "get_wishlist_count":get_wishlist_count,"get_wishlist":get_wishlist, "dilivery_chag": dilivery_chag, "total_amount": total_amount }

        return render(request,"shoping_cart.html",context)
    else:
        return render(request,"login.html")

def add_quantity(request,id):
    if 'email' in request.session: 
        if request.POST:
            uid = signup.objects.get(email = request.session['email'])
            get_cart = add_to_cart.objects.get(id=id,user_id=uid)
            get_cart.quantity = get_cart.quantity + 1           
            get_cart.total_prize = get_cart.quantity * get_cart.price 
            get_cart.save()
            return redirect('shoping_cart')
    else:
        return render(request,"login.html")        

def minus_quantity(request, id):
    if 'email' in request.session:
        if request.POST:
            uid = signup.objects.get(email=request.session['email'])
            try:
                get_cart = add_to_cart.objects.get(id=id, user_id=uid)
                if get_cart.quantity <= 1:  
                    get_cart.delete()
                else:    
                    get_cart.quantity -= 1           
                    get_cart.total_prize = get_cart.quantity * get_cart.price 
                    get_cart.save()
                return redirect('shoping_cart')
            except add_to_cart.DoesNotExist:
                return redirect('shoping_cart')
    else:
        return render(request, "login.html")


def wishlist(request):
    if 'email' in request.session:
        uid = signup.objects.get(email=request.session['email'])
        get_cart  = add_to_cart.objects.filter(user_id=uid)
        get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
        get_wishlist = wish_list.objects.filter(user_id = uid)
        get_wishlist_count = wish_list.objects.filter(user_id=uid).count()

        context = {"get_cart":get_cart,"get_cart_count":get_cart_count,"get_wishlist":get_wishlist,"get_wishlist_count":get_wishlist_count}
        return render(request, "wishlist.html",context)
    else:
        return render(request,"login.htmgl")

def add_to_wishlist(request,id):
    if 'email' in request.session:
        uid = signup.objects.get(email=request.session['email'])
        get_product = products.objects.get(id=id)
        wishlist_id = wish_list.objects.filter(products_id=get_product, user_id=uid)
        if wishlist_id:
            get_wishlist = wish_list.objects.get(products_id=get_product, user_id=uid)
            get_wishlist.delete()
            message = "item removed"
            messages.info(request,"product delete in whishlist")
        else:
            wish_list.objects.create(products_id=get_product, user_id=uid, name=get_product.name, img=get_product.img)    
            messages.info(request,"product save in whishlist")

            message = "item added"
        return redirect("index")
    else:
         return render(request,"login.htmgl")   
    
def coupon_apply(request):
    if 'email' in request.session:
        print(request.session['email'])
        uid = signup.objects.get(email=request.session['email'])
        get_cart  = add_to_cart.objects.filter(user_id=uid)
        get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
        get_wishlist = wish_list.objects.filter(user_id = uid)
        get_wishlist_count = wish_list.objects.filter(user_id=uid).count()
        cart_product_total_price = []
        get_subtotal = 0
        dilivery_chag = 100

        for i in get_cart:
            cart_product_total_price.append(i.total_prize)
        get_subtotal = sum(cart_product_total_price)
        total_amount = get_subtotal + dilivery_chag
        discount = 0

        if request.POST:
            coupon =  request.POST['code']
            coupon_code_id = coupon_code.objects.filter(code=coupon,one_time_use= True).exists()
            if coupon_code_id:
                coupon_codes = coupon_code.objects.get(code=coupon)
                now_time = timezone.now()
                coupon_codes.one_time_use = False
                coupon_codes.save()
                if coupon_codes.expiry_date > now_time:
                    total_amount = total_amount - coupon_codes.discount
                    discount = coupon_codes.discount
                    request.session['discount'] = discount
                    contaxt = {"dilivery_chag": dilivery_chag, "get_subtotal": get_subtotal, "uid": uid,
                               "get_cart": get_cart, "discount": discount, "total_amount": total_amount,
                               "get_cart_count": get_cart_count,"get_wishlist": get_wishlist, "get_wishlist_count": get_wishlist_count}
                    messages.success(request,"Coupon apply successfully......")
                    print(messages.success)
                    return  render(request, "shoping_cart.html",contaxt)
                else:
                    coupon_codes.delete()
                    contaxt = {"dilivery_chag": dilivery_chag, "get_subtotal": get_subtotal, "uid": uid,
                               "get_cart": get_cart, "discount": discount, "total_amount": total_amount,
                               "get_cart_count": get_cart_count,"get_wishlist": get_wishlist, "get_wishlist_count": get_wishlist_count}
                    messages.success(request,"Coupon has expired and has been deleted")
                    print(messages.success)
                    return  render(request, "shoping_cart.html",contaxt)
            else:
                messages.success(request, "No Discount in this code")
                return redirect("shoping_cart")
        return render(request, "shoping_cart.html")        
    else:
         return render(request,"login.htmgl")   

def address(request):
    if 'email' in request.session:
        uid = signup.objects.get(email=request.session['email'])
        get_cart  = add_to_cart.objects.filter(user_id=uid)
        get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
        get_wishlist = wish_list.objects.filter(user_id = uid)
        get_wishlist_count = wish_list.objects.filter(user_id=uid).count()
        get_address = Billing_detail.objects.filter(user_id = uid)
 
        all_product = []
        dilivery_chag = 100
        discount = 0
        total_amount = 0

        for i in get_cart:
            all_product.append(i.total_prize)
        get_subtotal = sum(all_product)
        total_amount = get_subtotal + dilivery_chag + discount

        if get_subtotal == 0 and "discount" in request.session:
            dilivery_chag = 0
            total_amount = 0
            del request.session['discount']
        else:
            dilivery_chag = 100

        if "discount" in request.session:
            discount = request.session.get("discount")
            total_amount = get_subtotal + dilivery_chag - discount
        else:
            discount = 0
            total_amount = get_subtotal + dilivery_chag

        #payment
        amount = max(total_amount, 1) * 100
        client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE', '77yKq3N9Wul97JVQcjtIVB5z'))
        response = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': 1})
        print(response,"")

        if request.method == 'POST':
            address_id = request.POST['address']
            print(address_id)
            if address_id:
                selected_address = Billing_detail.objects.get(id=address_id)
            
            for k in get_cart:
                order.objects.create(
                    order_id = response['id'],
                    user_id = uid,
                    address_id = selected_address,
                    name = k.name,
                    img = k.img,
                    description = "done",
                    size = k.size,
                    quantity = k.quantity,
                    price = k.price,
                    total_price = k.price * k.quantity,
                    status = "success"
                )
                k.delete()
            return redirect("orders")

        context = {"get_cart": get_cart,"get_cart_count":get_cart_count,"get_wishlist": get_wishlist,
                  "get_wishlist_count": get_wishlist_count,"get_address":get_address,
                  "get_subtotal": get_subtotal, "total_amount": total_amount, "dilivery_chag": dilivery_chag, "discount": discount,"response":response
                  }
        return render(request,"address.html",context)
    else:
        return render(request,"login.html") 

def add_address(request):
    if 'email' in request.session:
        uid = signup.objects.get(email=request.session['email'])
        
        if request.POST:
            name = request.POST['name']
            mobile_number = request.POST['mobile_number']
            pincode = request.POST['pincode']
            street_address = request.POST['street_address']
            town = request.POST['town']
            district = request.POST['district']
            state = request.POST['state']

            Billing_detail.objects.create(user_id = uid, full_name= name, mobile= mobile_number, pin_code= pincode, street_address=street_address, town= town, district= district, state= state)
            
            return redirect('address')
        return render(request,"address.html")
    else:
        return render(request,"login.html") 

def update_address(request,id):
    if 'email' in request.session:
        uid = signup.objects.get(email=request.session['email'])
        address_id = Billing_detail.objects.get(id=id)            
        print(address_id)
        
        if request.POST:
            name = request.POST['update_name']
            mobile_number = request.POST['update_mobile_number']
            pincode = request.POST['update_pincode']
            street_address = request.POST['update_street_address']
            town = request.POST['update_town']
            district = request.POST['update_district']
            state = request.POST['update_state']

            address_id.full_name = name
            address_id.mobile = mobile_number
            address_id.pin_code = pincode
            address_id.street_address = street_address
            address_id.town = town
            address_id.district = district
            address_id.state = state
            address_id.save()
            return redirect("address")
    
    else:
        return render(request,"login.html")

def delete_address(request,id):
    if 'email' in request.session:    
        uid = signup.objects.get(email=request.session['email'])
        print(id)
        address = Billing_detail.objects.get(id=id)
        address.delete()
        return redirect("address")
    else:
        return render(request,"login.html")

def orders(request):
    if 'email' in request.session:
        uid = signup.objects.get(email= request.session['email'])
        get_order  = order.objects.filter(user_id=uid)
        get_cart  = add_to_cart.objects.filter(user_id=uid)
        get_cart_count = add_to_cart.objects.filter(user_id=uid).count()
        get_wishlist = wish_list.objects.filter(user_id = uid)
        get_wishlist_count = wish_list.objects.filter(user_id=uid).count()

        
        contaxt = {"get_order": get_order, "uid": uid, "get_cart": get_cart, "get_cart_count" :get_cart_count,
                   "get_wishlist": get_wishlist, "get_wishlist_count": get_wishlist_count}
    return render(request, "order.html", contaxt)

def login(request):
    return render(request, "login.html")

def signups(request):
    return render(request, "signups.html")

def reset_pass(request):
    uid = signup.objects.get(email=request.session['email'])
    get_cart = add_to_cart.objects.filter(user_id=uid)

    context = {"get_cart": get_cart,} 
    return render(request, 'reset_pass.html',context)

def creates(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        response = requests.get(f"https://emailvalidation.abstractapi.com/v1/?api_key=6089bc4afeb248cfbae263ac6dd99ef8&email={email}")

        try:
            uid = signup.objects.get(email=email)
            message_for_email = "email already exist"
            return render(request,"signups.html",{"message_for_email":message_for_email})
        except:
               if response.status_code == 200:
                    data = response.json()
                    if data["deliverability"] == "DELIVERABLE":
                        if password == c_password:
                            if len(password) >= 8:
                                lower = []
                                uper = []
                                digit = []
                                special = []
                                for i in password:
                                    if i.islower():
                                        lower.append(i)
                                    elif i.isupper():
                                        uper.append(i)
                                    elif i.isdigit():
                                        digit.append(i)
                                    else:
                                        special.append(i)
                                if len(lower) == 0 or len(uper) == 0 or len(digit) == 0 or len(special) == 0 :
                                    message_for_password_critearia = "please create a strong password !"
                                    return render(request,"signups.html",{"message_for_password_critearia":message_for_password_critearia})
                                else:
                                    signup.objects.create(name=name,email=email,password=password)
                                    messages.success(request,'Registration are successfully completed.')
                                    return redirect("login")
                            else:
                                message_for_password_length = "password length must have 8 character"
                                return render(request,"signups.html",{"message_for_password_length":message_for_password_length})
                        else:
                            message_for_password = "please enter same password"
                            return render(request,"signups.html",{"message_for_password": message_for_password})
                    else:
                        message_for_email_valid = "email are not valid please enter the valid email."  
                        return render(request,'signups.html',{"message_for_email_valid" : message_for_email_valid} ) 

    else:
        return render(request,"signup.html")

def check_login(request):
    if "email" in request.session:
        uid = signup.objects.get(email = request.session['email'])
        return render(request,'index.html')
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        try :
            data= signup.objects.get(email=email , password=password)
            request.session['email']=data.email    
            return redirect('index')      
        except:
            massages_for_login = 'invilid user.... :)'
            return render(request, 'login.html', {"massages_for_login" : massages_for_login })

def log_out(request):
    if 'email' in request.session:
        del(request.session['email'])
        return redirect('login')
    else:
        return redirect('login')

def otp(request):
    if request.POST:
        email=request.POST['email']
        otp=random.randint(1000,9999)
        
        try:
            uid=signup.objects.get(email=email)
            uid.otp=otp
            uid.save()
            send_mail("Django",f"your OTP is :  {otp} don't share to any one. ","ishanbaraiya21@gmail.com",[email])
            context={"uid":uid,"email":email}
            return render(request,"reset_pass.html",context)
        except:
            return render(request,"otp.html")
    else:
        return render(request,"otp.html")

def check_otp(request):
    if request.POST:
        otp = request.POST['otp']
        password = request.POST['password']
        c_password = request.POST['c_password']

        try:
            uid = signup.objects.get(otp=otp)
            if uid.otp == otp:
                if password == c_password:
                    if len(password) >= 8:
                        lower = []
                        uper = []
                        digit = []
                        special = []
                        for i in password:
                            if i.islower():
                                lower.append(i)
                            elif i.isupper():
                                uper.append(i)
                            elif i.isdigit():
                                digit.append(i)
                            else:
                                special.append(i)
                        if len(lower) == 0 or len(uper) == 0 or len(digit) == 0 or len(special) == 0 :
                            message_for_password_critearia = "please create a strong password !"
                            return render(request,"reset_pass.html",{"message_for_password_critearia":message_for_password_critearia})
                        else:
                            uid.password = password
                            uid.otp = None  # Clear the OTP after successful password reset
                            uid.save()
                            messages.success(request, 'Your password has been updated sucessfully. :) ')
                            return redirect('login')
                    else:
                        message_for_password_length = "Password length must be at least 8 characters"
                        return render(request, "reset_pass.html", {"message_for_password_length": message_for_password_length, "otp": otp})
                else:
                    message_for_password = "Passwords do not match"
                    return render(request, "reset_pass.html", {"message_for_password": message_for_password, "otp": otp})
            else:
                message_for_otp = "Invalid OTP"
                return render(request, "reset_pass.html", {"message_for_otp": message_for_otp, "otp": otp})
        except signup.DoesNotExist:
            message_for_email = "Email does not exist"
            return render(request, "reset_pass.html", {"message_for_email": message_for_email, "otp": otp})
    else:
        return render(request, "reset_pass.html")    
# ---------------------------------------------------------------------------------------------------------------
