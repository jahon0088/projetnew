from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from base.format import formatget
from register.models import Product


class CRUDView(GenericAPIView):
    authentication_classes = TokenAuthentication,
    permission_classes = IsAuthenticated,

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            prods = Product.objects.filter(pk=pk).first()
            if not prods:
                return Response({"Error":"There is not such prod id"})
            return Response({"Result": formatget(prods)})

        pks = Product.objects.all()
        l = []
        for i in pks:
            l.append(formatget(i))
        return Response({"Result": l})

    def put(self, requests, pk, *args, **kwargs):
        data = requests.data
        prods = Product.objects.filter(pk=pk).first()

        if not prods:
            return Response({"Error": "Product not found"})

        serializer = self.get_serializer(data=data, instance=prods)
        serializer.is_valid(raise_exception=True)
        prods = serializer.save()
        return Response({"Result": formatget(prods)})

    def delete(self, requests, pk, *args, **kwargs):
        prods = Product.objects.filter(pk=pk).first()

        if not prods:
            return Response({"Error": "Product not found ! "})
        prods.delete()

        return Response({"Result": f"{pk} prod has been deleted"})
