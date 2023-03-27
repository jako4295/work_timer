import datetime as dt
import os


class WorkHandler:
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    foldername = ""
    current_file_path: str = None
    time_log_dir: str = None

    def __init__(self, time_log_dir: str):
        # check that the last character is a '/'
        if time_log_dir[-1] != '/':
            time_log_dir += '/'
        self.time_log_dir = time_log_dir

        # set the foldername
        if dt.datetime.now().day <= 15:
            idx = dt.datetime.now().month-1
            self.foldername += self.months[idx-1]
            self.foldername += "_"+ self.months[idx]
        else:
            idx = dt.datetime.now().month-1
            self.foldername += self.months[idx]
            self.foldername += "_"+ self.months[(idx+1)%12]
        
        self.current_file_path = self._get_current_file_path()
    
    
    def start(self):
        now = str(dt.datetime.now())[:16]
        if not os.path.isfile(self.current_file_path):
            os.makedirs(
                os.path.dirname(self.current_file_path),
                exist_ok=True
            )
            with open(self.current_file_path, "w") as f:
                f.write("start "+now)
        else:
            with open(self.current_file_path, 'r') as f:
                lines = f.readlines()
                if lines[-1][:5] == 'start':
                    raise Exception("You need to stop a timer first")
                    # we need to not raise exceptions, as they crash the program
                    # raise a warning instead
            
            with open(self.current_file_path, "a") as f:
                f.write('\nstart '+now)

    def stop(self):
        now = str(dt.datetime.now())[:16]

        if not os.path.exists(self.current_file_path):
            raise Exception("You need to start a timer first")

        with open(self.current_file_path, "r") as f:
            lines = f.readlines()
            if not lines[-1][:5] == 'start':
                raise Exception("You need to start a timer first")
            
        with open(self.current_file_path, "a") as f:
            f.write('\nstop '+now)

    def get_work_state(self) -> bool:
        if not os.path.exists(self.current_file_path):
            return False
        
        with open(self.current_file_path, "r") as f:
            lines = f.readlines()
            if lines[-1][:5] == 'start':
                return True
            else:
                return False
    
    def get_daily_log(self, ) -> str:
        with open(self.current_file_path, "r") as f:
            lines = f.readlines()
        
        return "".join(lines)


    def _get_current_file_path(self) -> str:
        now = str(dt.datetime.now())[:16]
        filename = "/"+now[:10]+".txt"

        return self.time_log_dir+self.foldername+filename


if __name__ == "__main__":
    wh = WorkHandler("/home/all/Timer Logs/")
    wh.start()
    