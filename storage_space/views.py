from django.shortcuts import render

# Create your views here.

class Profile(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        return JsonResponse({
            'First Name': customer.user.first_name,
            'Last Name': customer.user.last_name,
            'Username': customer.user.username,
            'Email': customer.user.email,
            'Biography': customer.bio,
            'Photo': customer.photo.url,
        })

    def post(self, request, format=None):
        user = request.user
        customer = Customer.objects.get(user=user)
        serializer = EditSerializer(customer, data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return HttpResponse(status=200)
        return JsonResponse(serializer.errors, status=400)

def dataMatrixDecoder(dataMatrix):
    dataMatrix = dataMatrix
    gs1list = [ #reminder to self add the name
    ('01',14,False,'Global Trade Item Number (GTIN)'),
    ('10',20,True,'Batch or Lot Number'),
    ('11',6,False,'Production Date (YYMMDD)'),
    ('13',20,True,'Packaging Date (YYMMDD)'),
    ('15',6,False,'Best Before Date (YYMMDD)'),
    ('17',20,True,'Expiration Date (YYMMDD)'),
    ('30',8,True,'Count of Items (Variable Measure Trade Item)'),
    ('310',6,False,'Net weight, kilograms (Variable Measure Trade Item)'),
    ('320',6,False,'Net weight, pounds (Variable Measure Trade Item)'),
    ('392',15,True,'Applicable Amount Payable, single monetary area (Variable Measure Trade Item)'),
    ('393',15,True,'Applicable Amount Payable with ISO Currency Code (Variable Measure Trade Item)'),
    ('395',6,False,'Amount payable per unit of measure single monetary area (variable measure trade item)'),
    ('412',13,False,'Purchased from Global Location Number'),
    ('414',13,False,'Identification of a Physical Location - Global Location Number'),
    ('422',3,False,'Country of Origin of a Trade Item'),
    ('8008',12,True,'Date and Time of Production')
    ]
    finalResult = []
    while dataMatrix:
        print('---------------------------------')
        print('DataMatrix')
        print(dataMatrix)
        head = dataMatrix[:4]
        length = search(gs1list, head[:2])
        if length != None:
            dataMatrix = dataMatrix[2:]
            if head[:2] == '11' or head[:2] == '13' or head[:2] == '15' or head[:2] == '17':
                print(length[3])
                result = ''
                for i in range(length[1]):
                    if not dataMatrix or dataMatrix[0] == '':
                        dataMatrix = dataMatrix[1:]
                        finalResult.append((int(length[0]),result))
                        break
                    result = result + dataMatrix[0]
                    dataMatrix = dataMatrix[1:]
                finalResult.append((int(length[0]),result[:2]+'-'+result[2:4]+'-'+result[4:]))
            else:
                print(length[3])
                result = ''
                for i in range(length[1]):
                    if not dataMatrix or dataMatrix[0] == '':
                        finalResult.append((int(length[0]),result))
                        break
                    result = result + dataMatrix[0]
                    dataMatrix = dataMatrix[1:]
                finalResult.append((int(length[0]),result))
            continue
        length = search(gs1list, head[:3])
        if length != None:
            if length[2]:
                print(length[3])
                dataMatrix = dataMatrix[3:]
                decimalPoints = length[1]-int(dataMatrix[0])
                dataMatrix = dataMatrix[1:]
                result = ''
                for i in range(length[1]):
                    if not dataMatrix or dataMatrix[0] == '':
                        dataMatrix = dataMatrix[1:]
                        result = result[:decimalPoints]+','+result[decimalPoints:]
                        finalResult.append((int(length[0]),result))
                        break
                    else:
                        result = result + dataMatrix[0]
                        dataMatrix = dataMatrix[1:]
                continue
            elif dataMatrix[0] == '3':
                print(length[3])
                dataMatrix = dataMatrix[3:]
                decimalPoints = 6-int(dataMatrix[0])
                dataMatrix = dataMatrix[1:]
                result = ''
                for i in range(length[1]):
                    result = result + dataMatrix[0]
                    dataMatrix = dataMatrix[1:]
                result = result[:decimalPoints]+','+result[decimalPoints:]
                finalResult.append((int(length[0]),result))
                continue
            else:
                print(length[3])
                dataMatrix = dataMatrix[3:]
                result = ''
                for i in range(length[1]):
                    result = result + dataMatrix[0]
                    dataMatrix = dataMatrix[1:]
                result = result[:decimalPoints]+','+result[decimalPoints:]
                finalResult.append((int(length[0]),result))
                continue
        length = search(gs1list, head[:4])
        if length != None:
            print(length[3])
            dataMatrix = dataMatrix[4:]
            for i in range(length[1]):
                result = result + dataMatrix[0]
                dataMatrix = dataMatrix[1:]
            finalResult.append((int(length[0]),result[:2]+'-'+result[2:4]+'-'+result[4:6]+' '+result[6:]))
            continue
        if length == None:
            print('______________________________')
            print('Failure, the following is the gs1 code')
            print(head)
            print(finalResult)
            return None
    return finalResult

def search(list,term):
    for i in range(len(list)):
        if(list[i][0]==term):
            return list[i]
    return None
