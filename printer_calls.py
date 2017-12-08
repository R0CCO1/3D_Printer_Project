import requests
import json
from datetime import timezone

class PrinterCalls:

    def get_status(self,printer_number):
        status=[]
        status.append(requests.get('http://10.76.100.'+printer_number+'/api/v1/printer/status'))
        status.append(status[0].text)
        return status

    def get_job_info(self, printer_number):
        if self.get_status(printer_number)[1] == '"idle"':
            return ""
        if self.get_status(printer_number)[1] == '"maintenance"':
            return ""
        else:
            info = requests.get('http://10.76.100.'+printer_number+'/api/v1/print_job')
            info = json.loads(info.text)
            results = []
            results.append(info["name"])
            datestart = info['datetime_started']
            #datestart = datestart.replace(tzinfo=timezone.utc).estimezone(tz=None)
            results.append(datestart)
            results.append(info["datetime_finished"])
            results.append(info["state"])
            time_elapsed=info['time_elapsed']
            results.append(time_elapsed)
            return results
