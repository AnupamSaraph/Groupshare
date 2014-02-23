from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from home.views import index
from login.views import *
#from employee.views import *
from employeeall.views import * 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home1),
    #url(r'^add/addemployee/$',contact),
    url(r'^addemployee/$',contact),
    url(r'^search/$',search),
	url(r'edit/(\d+)$',edit),
	url(r'^display/$',display),
	url(r'^find/$',find),	
	url(r'^edithistory/$',edithistory),
	url(r'^filterhistory/$',filteremp),
	url(r'emphis/(\d+)$',emphis),
	url(r'emp/(\d+)$',emp),
	url(r'empinfo/(\d+)$',empinfo),
	url(r'^addproject/$',addproject),
	url(r'^showproject/$',showproject),
	url(r'empproject/(\d+)$',empproject),
	url(r'^disemppro/$',disemppro),
	url(r'phonehis/(\d+)$',phonehis),
	url(r'designationhis/([\w ]+)$',designationhis),
	url(r'^addorganization/$',addorganization),
	url(r'^displayorg/$',displayOrg),
	url(r'editOrg/(\d+)$',editOrg),
	url(r'^adddepartment/$',addDepartment),
	url(r'^displaydept/$',displayDept),
	url(r'editDept/(\d+)$',editDept),
	url(r'orginfo/(\d+)$',orginfo),
	url(r'org_dept/(\d+)$',org_dept),
	url(r'deptinfo/(\d+)$',deptinfo),
	url(r'org_employee/(\d+)$',org_employee),
	url(r'dept_employee/(\d+)$',dept_employee),

    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += patterns('',
       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
{'document_root':'/static/'}),
    ) 


