from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,DetailView,CreateView,TemplateView,FormView,UpdateView
from customer.models import Categories
from django.urls import reverse_lazy
from .forms import BookingForm
from .models import Booking
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


# Create your views here.


def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect('signin')
    return inner
dec=[signin_required,never_cache]


class Userhome(ListView):
    template_name='userhome.html'
    model=Categories
    context_object_name='waste'

@method_decorator(dec,name="dispatch")
class BookingView(TemplateView):
    template_name='booking.html'
    # form_class=BookingForm
    # model=Booking
    # success_url=reverse_lazy('userh')
    context_object_name='item'

    def post(self,request,*args,**kwargs):
        bid=kwargs.get("bid")
        category=Categories.objects.get(id=bid)
        user=request.user
        address=request.POST.get("address")
        phone=request.POST.get("ph")
        bnum=request.POST.get("number_of_bags")
        date=request.POST.get("date")
        
        Booking.objects.create(type=category,cname=user,address=address,ph=phone,number_of_bags=bnum,date=date)

        return redirect('userh')
    

@method_decorator(dec,name="dispatch")
class BookedList(ListView):
    template_name='sclist.html'
    model=Booking
    context_object_name='booked'

    def get_queryset(self):
        return Booking.objects.filter(cname_id=self.request.user)
    



@method_decorator(dec,name="dispatch")
def delete(request,id):
    id=id
    Booking.objects.filter(id=id).delete()
    return redirect('userh')
    
    
    

# class Update(View):
    # model = Booking
    # form_class = BookingForm
    # template_name = "edit.html"

    # pk_url_kwarg = 'bookpk'
# ):
    # def get(self,request,*args,**kwargs):
    #     rid=kwargs.get("rid")
    #     rmdr=Booking.objects.get(id=rid)
    #     form=BookingForm(instance=rmdr)
    #     return render(request,'edit.html',{'form':form})
    # def post(self, request,*args,**kwargs):
    #     rid=kwargs.get("rid")
    #     rmdr=Booking.objects.get(id=rid)
    #     form_data=BookingForm(data=request.POST,instance=rmdr)
    #     if form_data.is_valid():
    #         form_data.save()
    #         messages.success(request,"Booking updated successfully")
    #         return redirect('blist')
    #     else:
    #         return render(request,'edit.html',{'form':form_data})
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # formdata=BookingForm( data=request.POST )
        # if formdata.is_valid():
        #     formdata.save()
        #     messages.success(self.request,"Booking Successful !!!")
        #     redirect('userh')
        # else:
        #     messages.error(self.request,"Booking Failed !!!")
        #     redirect('book')




    # def post(self, request,*args,**kwargs):
    #     formdata=BookingForm(data=request.POST)

    

