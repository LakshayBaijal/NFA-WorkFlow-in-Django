from django.shortcuts import render,redirect
from .models import Entry,Vendors,NeuralNet
from django.http.response import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
import torch
import json
import openai

# Create your views here.

def home(request):
    return render(request,'home.html')


def index(request): 
    entry = Entry.objects.all()
    vendor = Vendors.objects.all()
    
    context = {
        "entry" : entry,
        "vendor" : vendor
    }
    return render(request,'index.html',context)


def add(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        division = request.POST.get('division')
        subject_line = request.POST.get('subject_line')
        date = request.POST.get('date')
        summary = request.POST.get('summary')

        entry = Entry(
            project_name=project_name,
            division=division,
            subject_line=subject_line,
            date=date,
            summary=summary,
        )
        entry.save()
        return redirect('index')
    return render(request,'index.html')



def edit(request):
    entry = Entry.objects.all()
    context = {
        "entry" : entry
    }

    return redirect(request,'index.html',context)


def update(request,id):
    if request.method =="POST":
        project_name = request.POST.get('project_name')
        division = request.POST.get('division')
        subject_line = request.POST.get('subject_line')
        date = request.POST.get('date')
        summary = request.POST.get('summary')


        entry = Entry(
            id=id,
            project_name=project_name,
            division=division,
            subject_line=subject_line,
            date=date,
            summary=summary,
        )
        entry.save()
        return redirect('index')
    return redirect(request,'index.html')


def delete(request,id):
    entry = Entry.objects.filter(id=id).delete()
    context = {
        'entry':entry
    }

    return redirect('index')

def vendor_add(request):
    if request.method == 'POST':
        project = request.POST.get('project')
        vendor_name = request.POST.get('vendor_name')
        item_name = request.POST.get('item_name')
        total_base_value = request.POST.get('total_base_value')
        quantity = request.POST.get('quantity')
        unit_of_measurement = request.POST.get('unit_of_measurement')
        freight_charges = request.POST.get('freight_charges')
        pf_charges = request.POST.get('pf_charges')
        custom_duty = request.POST.get('custom_duty')
        installation_charges = request.POST.get('installation_charges')
        amc_charges = request.POST.get('amc_charges')
        third_party_inspection_charges = request.POST.get('third_party_inspection_charges')
        other_charges = request.POST.get('other_charges')
        total_value = request.POST.get('total_value')
        gst = request.POST.get('gst')
        landed_cost = request.POST.get('landed_cost')
        delivery = request.POST.get('delivery')
        payment_terms = request.POST.get('payment_terms')
        remark = request.POST.get('remark')


        vendor = Vendors(
            project=project,
            vendor_name=vendor_name,
            item_name=item_name,
            total_base_value=total_base_value,
            quantity=quantity,
            unit_of_measurement=unit_of_measurement,
            freight_charges=freight_charges,
            pf_charges=pf_charges,
            custom_duty=custom_duty,
            installation_charges=installation_charges,
            amc_charges=amc_charges,
            third_party_inspection_charges=third_party_inspection_charges,
            other_charges=other_charges,
            total_value=total_value,
            gst=gst,
            landed_cost=landed_cost,
            delivery=delivery,
            payment_terms=payment_terms,
            remark=remark,
        )
        vendor.save()
        return redirect('index')
    return render(request,'index.html')


def vendor_edit(request):
    vendor = Vendors.objects.all()
    context = {
        "vendor" : vendor
    }

    return redirect(request,'index.html',context)


def vendor_update(request,id):
    if request.method =="POST":
        project = request.POST.get('project')
        vendor_name = request.POST.get('vendor_name')
        item_name = request.POST.get('item_name')
        total_base_value = request.POST.get('total_base_value')
        quantity = request.POST.get('quantity')
        unit_of_measurement = request.POST.get('unit_of_measurement')
        freight_charges = request.POST.get('freight_charges')
        pf_charges = request.POST.get('pf_charges')
        custom_duty = request.POST.get('custom_duty')
        installation_charges = request.POST.get('installation_charges')
        amc_charges = request.POST.get('amc_charges')
        third_party_inspection_charges = request.POST.get('third_party_inspection_charges')
        other_charges = request.POST.get('other_charges')
        total_value = request.POST.get('total_value')
        gst = request.POST.get('gst')
        landed_cost = request.POST.get('landed_cost')
        delivery = request.POST.get('delivery')
        payment_terms = request.POST.get('payment_terms')
        remark = request.POST.get('remark')

        vendor = Vendors(
            id=id,
            project=project,
            vendor_name=vendor_name,
            item_name=item_name,
            total_base_value=total_base_value,
            quantity=quantity,
            unit_of_measurement=unit_of_measurement,
            freight_charges=freight_charges,
            pf_charges=pf_charges,
            custom_duty=custom_duty,
            installation_charges=installation_charges,
            amc_charges=amc_charges,
            third_party_inspection_charges=third_party_inspection_charges,
            other_charges=other_charges,
            total_value=total_value,
            gst=gst,
            landed_cost=landed_cost,
            delivery=delivery,
            payment_terms=payment_terms,
            remark=remark,
        )
        vendor.save()
        return redirect('index')
    return redirect(request,'index.html')


def vendor_delete(request,id):
    vendor = Vendors.objects.filter(id=id).delete()
    context = {
        'vendor': vendor
    }

    return redirect('index')



def view_project(request,id):
    entry = Entry.objects.get(id=id)
    vendor = Vendors.objects.all()
    context = {
        "entry" : entry,
        "vendor" : vendor
    }

    return render(request,'view_project.html',context)






def chatget(request):
    return render(request,'bot.html')


def chatpost(request):
    openai.api_key = "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"    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open('intents.json', 'r') as json_data:
        intents = json.load(json_data)

    FILE = "data.pth"
    data = torch.load(FILE)
    response = CustomChatGPT(data)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()
        

    return render(request,'bot.html')



def CustomChatGPT(user_input):
    openai.api_key = "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"    

    messages = [{"role": "system", "content": "You give guidance"}]
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    messages.append({"role": "assistant", "content": "ChatGPT_reply"})
    return response
