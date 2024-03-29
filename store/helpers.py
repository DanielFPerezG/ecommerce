import json
import random
import string

from django.conf import settings
from base.models import Cupon

class ProductCart:

    def numberProducts(cart):
        productCarts = json.loads(cart.products)
        numberProductsCart = 0
        for productJson in productCarts:
            numberProductsCart += 1

        return numberProductsCart

    def newProductCart(cart, newProduct):
        newProductCarts = []
        productCarts = json.loads(cart.products)
        for productJson in productCarts:
            if int(productJson["id"]) == int(newProduct.id):
                newProductCarts.append(productJson)

        return newProductCarts

    def productCartWithStock(cart, products):
        productCart = json.loads(cart.products)
        productCartWithStock = []

        for item in productCart:
            productId = item['id']
            productName = item['name']
            price = item['price']
            image_url = item['image_url']
            productTotal = item['total']
            quantity = item['quantity']
            product = products.get(pk=productId)
            stock = product.stock
            itemWithStock = {
                'id': productId,
                'name': productName,
                'price': price,
                'image_url': image_url,
                'total': productTotal,
                'quantity': quantity,
                'stock': stock,
            }
            productCartWithStock.append(itemWithStock)

        return productCartWithStock

    def productCartWithStockCheckout(cart, products):
        productCart = json.loads(cart.products)
        productCartWithStock = []

        for item in productCart:
            productId = item['id']
            productName = item['name']
            price = item['price']
            image_url = item['image_url']
            productTotal = item['total']
            quantity = item['quantity']
            product = products.get(pk=productId)
            stock = product.stock

            if int(quantity) > int(stock):
                productTotal = int(price)*int(stock)
                quantity = stock
            itemWithStock = {
                'id': productId,
                'name': productName,
                'price': price,
                'image_url': image_url,
                'total': productTotal,
                'quantity': quantity,
                'stock': stock,
            }
            productCartWithStock.append(itemWithStock)

        return productCartWithStock

    def productCartWithStockCreateOrder(cart, products):
        productCart = json.loads(cart.products)
        productCartWithStock = []

        for item in productCart:
            productId = item['id']
            productName = item['name']
            image_url = item['image_url']
            quantity = item['quantity']
            product = products.get(pk=productId)
            stock = product.stock
            if cart.cupon:
                price = item['price'] - (item['price'] * cart.cupon.value / 100)
                productTotal = item['total'] - (item['total'] * cart.cupon.value / 100)
            else:
                price = item['price']
                productTotal = item['total']

            if int(quantity) > int(stock):
                productTotal = int(price)*int(stock)
                quantity = stock
            itemWithStock = {
                'id': productId,
                'name': productName,
                'price': price,
                'image_url': image_url,
                'total': productTotal,
                'quantity': quantity,
                'stock': stock,
            }
            if cart.cupon:
                itemWithStock['cupon'] = cart.cupon.pk

            productCartWithStock.append(itemWithStock)

        return productCartWithStock


    def subtotalCart(cart, page):
        subTotal = 0

        if page == 'cart':
            productCarts = json.loads(cart.products)

            for productJson in productCarts:
                subTotal += productJson['total']

            return subTotal
        elif page == 'createOrder':
            if cart.cupon:
                for item in cart:
                    subTotal += item['total'] - (item['total'] * cart.cupon.value / 100)
            else:
                for item in cart:
                    subTotal += item['total']
        else:
            for item in cart:
                subTotal += item['total']

            return subTotal

class CuponAdmin:

    def generateFirstCupon(request):
        prefix = "10OFF"
        suffix = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        return prefix + suffix
    def FirstOrderCupon(user):
        value = settings.DISCOUNT_PERCENTAGE
        cupon = str(CuponAdmin.generateFirstCupon(user))

        newCupon = Cupon.objects.create(
            cupon = cupon,
            quantity = 1,
            description = f'{value}% de descuento ¡por tu primera compra!',
            user = user,
            value = value
        )
        newCupon.save()

        return newCupon




