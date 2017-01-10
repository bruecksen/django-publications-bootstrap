__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

import re
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.db import transaction
from publications.models import Publication, Type
from publications.utils import import_bibtex as do_import_bibtex

# mapping of months
MONTHS = {
    'jan': 1, 'january': 1,
    'feb': 2, 'february': 2,
    'mar': 3, 'march': 3,
    'apr': 4, 'april': 4,
    'may': 5,
    'jun': 6, 'june': 6,
    'jul': 7, 'july': 7,
    'aug': 8, 'august': 8,
    'sep': 9, 'september': 9,
    'oct': 10, 'october': 10,
    'nov': 11, 'november': 11,
    'dec': 12, 'december': 12}


def import_bibtex(request):
	if request.method == 'POST':
		# try to import BibTex
		bibtex = request.POST['bibliography']

		with transaction.atomic():
			publications, errors = do_import_bibtex(bibtex)

		status = messages.SUCCESS
		if len(publications) == 0:
			status = messages.ERROR
			msg = 'No publications were added, %i errors occurred' % len(errors)
		elif len(publications) > 1:
			msg = 'Successfully added %i publications (%i skipped due to errors)' % (len(publications), len(errors))
		else:
			msg = 'Successfully added %i publication (%i error(s) occurred)' % (len(publications), len(errors))

		# show message
		messages.add_message(request, status, msg)

		for error in errors:
			messages.add_message(request, messages.ERROR, error)

			# redirect to publication listing
			if len(publications) == 1:
				return HttpResponseRedirect('../%s/change/' % publications[0].id)
			else:
				return HttpResponseRedirect('../')
	else:
	    return render(
			request,
					'admin/publications/import_bibtex.html', {
					'title': 'Import BibTex',
					'types': Type.objects.all(),
					'request': request})


import_bibtex = staff_member_required(import_bibtex)
