#coding: utf-8 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from cto.goal.models import Report, Goal
from django.db.models import Q


class GoalAdmin(admin.ModelAdmin):
    fields = ['choice']    
    def queryset(self, request):
        """
        Filter the objects displayed in the change_list to only
        display those for the currently signed in user.
        """
        qs = super(GoalAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(Q(user=request.user) | Q(user=request.user))
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
        
class LifeAdmin(admin.ModelAdmin):
    fields = ['message', 'publication_date']
    list_display = ('publication_date', 'message')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
        
    def queryset(self, request):
        """
        Filter the objects displayed in the change_list to only
        display those for the currently signed in user.
        """
        qs = super(LifeAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(Q(user=request.user) | Q(user=request.user))


    
admin.site.register(Report, LifeAdmin)
admin.site.register(Goal, GoalAdmin)
