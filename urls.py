
urlpatterns += patterns ('',
 (r'^bookapp/', include('bookapp.urls')),
 (r'book/edit/(?P<id>[^/]+)/$', edit_book),
)
