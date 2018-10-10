
import re
def retime(file):
    if file=="":
        file="mongod.log"
    fr=open(file=file,mode="r+",encoding="utf-8")
    content=fr.read()
    print(content)
    mat = re.findall(r"(\d{4}-\d{1,2}-\d{1,2}T\d{1,2}:\d{1,2})", content)
    print(mat)
    return  mat

def filew(mode,content:str):
    fr = open(file="result.txt", mode=mode, encoding="utf-8")
    fr.write(content)
    fr.close()
if __name__=="__main__":
    fw=retime("")
    content=",\n".join(fw)
    filew("a",content)

