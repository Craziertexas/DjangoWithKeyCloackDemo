class StandarQuerys():

    def __init__(self, Model, QueryParams, OutSerializer = None):
        self.QueryParams = QueryParams
        self.Model = Model
        self.OutSerializer = OutSerializer

    def GetObject(self):
        model = self.Model.objects

        if ("$filter" in self.QueryParams):
            query = self.QueryParams["$filter"]
            query = dict(e.split('=') for e in query.split(','))
            model = model.filter(**query)
        else:
            model = model.all()
        
        fields = [f.name for f in self.Model._meta.get_fields()]

        if ("$exclude" or "$select" in self.QueryParams):
            if ("$exclude" in self.QueryParams):
                excludedFields = self.QueryParams["$exclude"].split(',')
                for excludedField in excludedFields:
                    fields.remove(excludedField)
            elif ("$select" in self.QueryParams):
                fields = []
                selectFields = self.QueryParams["$select"].split(',')
                for selectField in selectFields:
                    fields.append(selectField)

        if ("$expand" in self.QueryParams):
            if ((self.QueryParams["$expand"] == "True") and (self.OutSerializer != None)):
                return self.OutSerializer(model,many=True,fields=fields).data
            else:
                return model.values(*fields)
        else:
            return model.values(*fields)
        