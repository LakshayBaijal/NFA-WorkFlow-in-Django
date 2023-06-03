from django.db import models
import torch
import torch.nn as nn 



class Entry(models.Model):
    project_name = models.CharField(max_length=15)
    division = models.CharField(max_length=30,blank=True)
    subject_line = models.CharField(max_length=30,blank=True)
    date = models.DateField(auto_now=True,blank=True)
    summary = models.TextField(max_length=50,blank=True)



    def __str__(self):
        return str(self.project_name)
    
class Vendors(models.Model):
    project = models.CharField(max_length=20)
    vendor_name = models.CharField(max_length=20,null=True,blank=True)
    item_name = models.CharField(max_length=20,null=True,blank=True)
    total_base_value = models.CharField(max_length=20,null=True,blank=True)
    quantity = models.CharField(max_length=20,null=True,blank=True)
    unit_of_measurement = models.CharField(max_length=10,null=True,blank=True)
    freight_charges = models.CharField(max_length=10,null=True,blank=True)
    pf_charges = models.CharField(max_length=10,null=True,blank=True)
    custom_duty = models.CharField(max_length=10,null=True,blank=True)
    installation_charges = models.CharField(max_length=10,null=True,blank=True)
    amc_charges = models.CharField(max_length=10,null=True,blank=True)
    third_party_inspection_charges = models.CharField(max_length=10,null=True,blank=True)
    other_charges = models.CharField(max_length=10,null=True,blank=True)
    total_value = models.CharField(max_length=10,null=True,blank=True)
    gst = models.CharField(max_length=10,null=True,blank=True)
    landed_cost = models.CharField(max_length=10,null=True,blank=True)
    delivery = models.CharField(max_length=10,null=True,blank=True)
    payment_terms = models.CharField(max_length=10,null=True,blank=True)
    remark = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return str(self.vendor_name) 
    


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size,num_classes):
        super(NeuralNet,self).__init__()
        
        self.l1=nn.Linear(input_size,hidden_size)
        self.l2=nn.Linear(hidden_size,hidden_size)
        self.l3=nn.Linear(hidden_size,num_classes)
        self.relu=nn.ReLU()


    def forward(self,x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)

        return out 

class FeedBack(models.Model):
    feedback_choice =  (('Great','Great'),('Average','Average'),('Poor','Poor'))
    feedback = models.CharField(max_length=15,choices=feedback_choice,blank=True)
    def __str__(self):
        return str(self.feedback) 
    
