import json
import pandas as pd

def check_num_type():
    lst = []
    in_file = open('dataset/train_base.json','r')
    for line in in_file:
        line = line.strip()
        line = json.loads(line)
        #print(line)
        ids = line['id']
        content = line['content']
        for k in line['events']:
            evn_type = k['type']
            lst.append(evn_type)
    lst = set(lst)
    print(lst)
    
def change_data():
    in_file = open('dataset/train_base.json','r')
    final_lst = []
    for line in in_file:
        # org_lst = ['质押','股份股权转让','起诉','投资','减持']
        # org_lst = ['Business:Declare-Bankruptcy','Business:End-Org','Business:Merge-Org','Business:Start-Org','Conflict:Attack','Conflict:Demonstrate','Contact:Meet','Contact:Phone-Write','Justice:Acquit','Justice:Appeal','Justice:Arrest-Jail','Justice:Charge-Indict','Justice:Convict','Justice:Extradite','Justice:Fine','Justice:Pardon','Justice:Release-Parole','Justice:Sentence','Justice:Sue','Justice:Trial-Hearing','Life:Be-Born','Life:Die','Life:Divorce','Life:Injure','Life:Marry','Movement:Transport','Personnel:Elect','Personnel:End-Position','Personnel:Nominate','Personnel:Start-Position','Transaction:Transfer-Money','Transaction:Transfer-Ownership']
        org_lst = ['BusinessDeclareBankruptcy','BusinessEndOrg','BusinessMergeOrg','BusinessStartOrg','ConflictAttack','ConflictDemonstrate','ContactMeet','ContactPhoneWrite','JusticeAcquit','JusticeAppeal','JusticeArrestJail','JusticeChargeIndict','JusticeConvict','JusticeExtradite','JusticeFine','JusticePardon','JusticeReleaseParole','JusticeSentence','JusticeSue','JusticeTrialHearing','LifeBeBorn','LifeDie','LifeDivorce','LifeInjure','LifeMarry','MovementTransport','PersonnelElect','PersonnelEndPosition','PersonnelNominate','PersonnelStartPosition','TransactionTransferMoney','TransactionTransferOwnership']
        line = line.strip()
        line = json.loads(line)
        #print(line)
        ids = line['id']
        content = line['content']
        lst = []
        for k in line['events']:
            if len(k)==1:
                continue
            evn_type = k['type']
            lst.append(evn_type)
        #print(ids,content,lst)
        label_lst = []
        label_lst.append(ids)
        label_lst.append(content)
        for i in org_lst:
            if i in lst:
                label_lst.append(1)
            else:
                label_lst.append(0)
        #print(label_lst)
        final_lst.append(label_lst)
    return final_lst

def get_cls_train_data():
    final_lst = change_data()
    df = pd.DataFrame()
    df = df.append(final_lst,ignore_index=True)
    df.columns = ['id','content','Bankruptcy','EndOrg','MergeOrg','StartOrg','Attack','Demonstrate','Meet','PhoneWrite','Acquit','Appeal','Jail','Indict','Convict','Extradite','Fine','Pardon','Parole','Sentence','Sue','Hearing','Born','Die','Divorce','Injure','Marry','Transport','Elect','EndPosition','Nominate','StartPosition','Money','Ownership']

    df.to_csv('TC/pybert/dataset/train_sample.csv',index=0)
    print('分类模型训练集已转换完成！')
    
def get_cls_test_data():
    test_df = open('dataset/dev_base.json')
    lst=[]
    for line in test_df:
        line = line.strip()
        line = json.loads(line)
        #print(line)
        lst.append(line)
    df = pd.DataFrame(lst)
    df = df[['id','content']]
    df.to_csv('TC/pybert/dataset/test.csv',index=0)
    print('分类模型测试集已转换完成！')
    
if __name__ == '__main__':
    get_cls_train_data()
    get_cls_test_data()
