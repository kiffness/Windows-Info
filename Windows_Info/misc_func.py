# This serves as a place to put all my misc functions

def format_text():
        with open (r'f:\Windows_10_Refresh\Powershell\SysConfig.txt', 'r') as f:
    
   
            lines = f.read().splitlines()
            
            if lines[6] == '24':
                lines.insert(6,"DDR4")
                del lines[7]
            elif lines[6] == '23':
                lines.insert(6,"DDR3")
                del lines[7]
            elif lines[6] == '22':
                lines.insert(6,"DDR2")
                del lines[7]
            elif lines[6] == '21':
                lines.insert(6,"DDR")
                del lines[7]
                
        return lines


