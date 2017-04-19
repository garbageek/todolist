from django.conf.urls import url
from .views import TaskList
from .views import TaskCreate
from .views import TaskDetail
from .views import TaskUpdate
from .views import TaskDelete
from .views import task_populate
from .views import task_delete_all

urlpatterns = [
    url(r'^$', TaskList.as_view(), name='task-list'),
    url(r'^add/$', TaskCreate.as_view(), name='task-add'),
    url(r'^populate/$', task_populate, name='task-populate'),
    url(r'^delete-all/$', task_delete_all, name='task_delete_all'),
    url(r'^(?P<pk>[0-9]+)/detail/$', TaskDetail.as_view(), name='task-detail'),
    url(r'^(?P<pk>[0-9]+)/$', TaskUpdate.as_view(), name='task-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', TaskDelete.as_view(), name='task-delete'),
]
