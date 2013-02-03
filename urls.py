from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('tracker.views',
	url(r'^challenges/(?P<event>\d+|)$', 'challengeindex'),
	url(r'^challenge/(?P<id>-?\d+)$', 'challenge'),
	url(r'^choices/(?P<event>\d+|)$', 'choiceindex'),
	url(r'^choice/(?P<id>-?\d+)$', 'choice'),
	url(r'^choiceoption/(?P<id>-?\d+)$', 'choiceoption'),
	url(r'^donors/(?P<event>\d+|)$', 'donorindex'),
	url(r'^donor/(?P<id>-?\d+)/(?P<event>\d+|)$', 'donor'),
	url(r'^donations/(?P<event>\d+|)$', 'donationindex'),
	url(r'^donation/(?P<id>-?\d+)$', 'donation'),
	url(r'^runs/(?P<event>\d+|)$', 'runindex'),
	url(r'^run/(?P<id>-?\d+)$', 'run'),
	url(r'^prizes/(?P<event>\d+|)$', 'prizeindex'),
	url(r'^prize/(?P<id>-?\d+)$', 'prize'),
	url(r'^prize_donors/(?P<id>-?\d+)$', 'prize_donors'),
	url(r'^draw_prize/(?P<id>-?\d+)$', 'draw_prize'),
	url(r'^merge_schedule/(?P<id>-?\d+)$', 'merge_schedule'),
	url(r'^events/$', 'eventlist'),
	url(r'^setusername/$', 'setusername'),
	url(r'^i18n/', include('django.conf.urls.i18n')),
	url(r'^search/$', 'search'),
	url(r'^add/$', 'add'),
	url(r'^edit/$', 'edit'),
	url(r'^delete/$', 'delete'),
	url(r'^index/(?P<event>\d+|)$', 'index'),
	url(r'^donation_edit/$', 'donation_edit', name='donation_edit'),
	url(r'^(?P<event>\d+|)$', 'index'),
	url(r'^paypal/(?P<event>\d+)$', 'paypal'),
	url(r'^paypal_return/$', 'paypal_return', name='paypal_return'),
	url(r'^paypal_cancel/$', 'paypal_cancel', name='paypal_cancel'),
	url(r'^ipn/$', 'ipn', name='ipn'),
        url(r'^donation_edit_auth/$', 'donation_edit_auth', name='donation_edit_auth'),
)

