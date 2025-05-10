# Příklady použití field lookups:

# 1. exact - přesná shoda
movies1 = Movie.objects.filter(title__exact="Inception")

# 2. iexact - přesná shoda bez ohledu na velikost písmen
movies2 = Movie.objects.filter(title__iexact="inception")

# 3. contains - řetězec obsahuje zadaný text
movies3 = Movie.objects.filter(title__contains="Inc")

# 4. icontains - řetězec obsahuje zadaný text (ignoruje velikost písmen)
movies4 = Movie.objects.filter(title__icontains="inc")

# 5. in - hodnota se nachází v daném seznamu hodnot
movies5 = Movie.objects.filter(genre__name__in=["Action", "Drama"])

# 6. gt (greater than) - větší než
movies6 = Movie.objects.filter(rating__gt=8.0)

# 7. gte (greater than or equal) - větší nebo rovno
movies7 = Movie.objects.filter(rating__gte=8.0)

# 8. lt (less than) - menší než
movies8 = Movie.objects.filter(rating__lt=7.0)

# 9. lte (less than or equal) - menší nebo rovno
movies9 = Movie.objects.filter(rating__lte=7.0)

# 10. startswith - začíná zadaným řetězcem
movies10 = Movie.objects.filter(title__startswith="The")

# 11. istartswith - začíná zadaným řetězcem (ignoruje velikost písmen)
movies11 = Movie.objects.filter(title__istartswith="the")

# 12. endswith - končí zadaným řetězcem
movies12 = Movie.objects.filter(title__endswith="man")

# 13. iendswith - končí zadaným řetězcem (ignoruje velikost písmen)
movies13 = Movie.objects.filter(title__iendswith="man")

# 14. range - hodnota spadá do zadaného rozsahu
movies14 = Movie.objects.filter(release_date__range=["2020-01-01", "2020-12-31"])

# 15. date - přesná shoda data (vhodné u DateTimeField)
movies15 = Movie.objects.filter(release_date__date="2020-05-20")

# 16. year - filtr podle roku
movies16 = Movie.objects.filter(release_date__year=2020)

# 17. month - filtr podle měsíce
movies17 = Movie.objects.filter(release_date__month=5)

# 18. day - filtr podle dne
movies18 = Movie.objects.filter(release_date__day=20)

# 19. week_day - filtr podle dne v týdnu (Neděle = 1, Pondělí = 2, atd.)
movies19 = Movie.objects.filter(release_date__week_day=2)

# 20. isnull - hledání záznamů, kde je pole null
movies20 = Movie.objects.filter(genre__isnull=True)

# 21. search - fulltextové vyhledávání (závisí na konfiguraci databáze)
movies21 = Movie.objects.filter(description__search="thriller")

# 22. regex - filtrování pomocí regulárního výrazu
movies22 = Movie.objects.filter(title__regex=r'^The.*')

# 23. iregex - regulární výraz ignorující velikost písmen
movies23 = Movie.objects.filter(title__iregex=r'^the.*')