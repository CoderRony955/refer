import os


class Validate:
    @staticmethod
    def path(path: str):
        """Validate given path 
        """
        try:
            target_path = ""
            if path.startswith("\'"):
                target_path = path.replace("\'", "")
                
            elif path.startswith("\"", ""):
                target_path = path.replace("\"", "")
                
            if not os.path.exists(path=target_path):
                return False
            return True
        except Exception as e:
            return e
