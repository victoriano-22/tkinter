class ModelData:
    def __init__(self, obj_data):
        try:
            # self.notif = obj_data['notif']
            self.order = obj_data['order']
            self.opsno = obj_data['opsno']
            self.measure_point = obj_data['measure_point']
            self.revision =  obj_data['revision']
            self.posting_date = obj_data['posting_date']
            self.usv_name = obj_data['usv_name']
            self.x = 'X'
            self.start = obj_data['start']
            self.end = obj_data['end']
            self.sta = obj_data['sta']
            self.spasi_empatbls = "              "
            self.ogl = round(obj_data['ogl'], 3)
            self.da = round(obj_data['da'], 3)
            self.db = round(obj_data['db'], 3)
            self.spasi_dua = '  '
            self.oc = "AX"
        except KeyError:
            pass