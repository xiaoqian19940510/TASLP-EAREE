import json
import pandas as pd
import random


def change_data():
    in_file = open('dataset/train_base.json','r')
    final_lst = []
    for line in in_file:
        line = line.strip()
        line = json.loads(line)
        ids = str(line['id'])
        content = line['content']
        for k in line['events']:
            if len(k)==1:
                continue
            evn_type = k['type']
            role_lst = []
            for i in k['mentions']:
                n = str(random.randint(0, 7))
                ids = ids+'_'+n
                lst = []
                word = i['word']
                start_span = i['span'][0]
                end_span = i['span'][1]
                role = i['role']
                role_lst.append(role)
                all_lst = [ids,content,evn_type,word,start_span,role,end_span]
                final_lst.append(all_lst)
            if evn_type=='BusinessDeclareBankruptcy':
                role_all = ['Org','Time-Within','trigger']
            elif evn_type=='BusinessEndOrg':
                role_all = ['trigger','Org', 'Time-Within','Person','Place','Beneficiary']
            elif evn_type=='BusinessMergeOrg':
                role_all = ['Org','Time-Starting','Place','trigger','Seller','Buyer','Time-Within','Time-Before','Time-Ending']
            elif evn_type=='BusinessStartOrg':
                role_all = ['Org','Agent','Time-Within','Place','Time-Starting','trigger','Time-Before','Time-After','Person','Destination']
            elif evn_type=='ConflictAttack':
                role_all = ['trigger','Place','Entity','Time-Within','Agent','Destination','Attacker','Time-Starting','Time-Ending','Victim','Person','Origin','Instrument','Time-Holds','Defendant','Target','Crime','Artifact','Time-Before','Vehicle','Org','Time-After','Adjudicator','Plaintiff','Sentence','Time-At-End','Time-At-Beginning','Position']
            elif evn_type=='ConflictDemonstrate':
                role_all = ['Place','Entity','Time-Within','trigger','Person','Time-Before','Attacker','Target','Time-Starting','Vehicle','Artifact','Destination','Origin','Time-Holds','Time-After']
            elif evn_type=='ContactMeet':
                role_all = ['trigger','Entity','Time-Within','Place','Org','Agent','Time-Holds','Person','Destination','Defendant','Time-Ending','Time-Before','Time-After','Time-Starting']
            elif evn_type=='ContactPhoneWrite':
                role_all = ['Entity','trigger','Time-Within','Adjudicator','Defendant','Crime','Place','Time-Before','Time-Starting']
            elif evn_type=='JusticeAcquit':
                role_all = ['trigger','Defendant','Crime','Adjudicator','Place']
            elif evn_type=='JusticeAppeal':
                role_all = ['trigger','Plaintiff','Adjudicator','Time-Within','Person','Agent','Time-Starting','Defendant','Place','Time-Holds','Time-At-Beginning','Time-Before','Time-Ending','Giver','Money','Recipient']
            elif evn_type=='JusticeArrestJail':
                role_all = ['trigger','Person','Agent','Place','Time-Within','Time-Holds','Time-Ending','Time-Starting','Destination','Time-Before','Crime','Defendant','Sentence','Entity','Position']
            elif evn_type=='JusticeChargeIndict':
                role_all = ['Defendant','Adjudicator','Time-Within','Prosecutor','Crime','trigger','Place','Time-After','Person','Destination']
            elif evn_type=='JusticeConvict':
                role_all = ['Defendant','Giver','Money','Place','trigger','Adjudicator','Time-Within','Crime','Time-After']
            elif evn_type=='JusticeExtradite':
                role_all = ['trigger','Person','Agent','Origin','Destination','Crime']
            elif evn_type=='JusticeFine':
                role_all = ['trigger','Entity','Money','Adjudicator','Crime','Time-Within','Place']
            elif evn_type=='JusticePardon':
                role_all = ['Defendant','Adjudicator','Time-Within','trigger']
            elif evn_type=='JusticeReleaseParole':
                role_all = ['Person','Place','Agent','Time-Within','trigger','Crime','Entity','Defendant','Adjudicator']
            elif evn_type=='JusticeSentence':
                role_all = ['trigger','Defendant','Sentence','Crime','Adjudicator','Time-Within','Plaintiff','Place','Time-After','Time-Holds','Org']
            elif evn_type=='JusticeSue':
                role_all = ['Adjudicator','Defendant','trigger','Crime','Plaintiff','Time-Within','Place','Time-Starting','Person','Entity','Time-Ending']
            elif evn_type=='JusticeTrialHearing':
                role_all = ['Adjudicator','Defendant','Crime','Time-Starting','trigger','Time-Within','Time-At-End','Person','Entity','Time-Ending','Place','Time-At-Beginning','Agent','Sentence','Time-Holds','Plaintiff','Position','Org','Destination','Prosecutor','Time-Before']
            elif evn_type=='LifeBeBorn':
                role_all = ['trigger','Person','Place','Time-Within','Agent','Origin']
            elif evn_type=='LifeDie':
                role_all = ['Agent','Destination','trigger','Victim','Place','Time-Within','Time-After','Time-Before','Attacker','Target','Instrument','Time-Starting','Time-Holds','Entity','Time-Ending','Person','Origin']
            elif evn_type=='LifeDivorce':
                role_all = ['trigger','Person']
            elif evn_type=='LifeInjure':
                role_all = ['Adjudicator','Defendant','Place','Sentence','Crime','Time-Within','Instrument','Victim','Agent','Time-Holds','Time-Starting','trigger','Attacker','Target','Time-Ending']
            elif evn_type=='LifeMarry':
                role_all = ['Person','Place','Time-Within','trigger','Time-After','Time-Holds']
            elif evn_type=='MovementTransport':
                role_all = ['trigger','Vehicle','Destination','Origin','Time-Before','Person','Time-Within','Time-Holds','Attacker','Target','Time-Ending','Time-After','Agent','Time-Starting','Artifact','Place','Position','Entity','Victim','Time-At-End','Time-At-End','Time-At-Beginning','Time-At-End','Time-At-End']
            elif evn_type=='PersonnelElect':
                role_all = ['trigger','Person','Place','Entity','Time-Within','Time-Holds','Adjudicator','Plaintiff','Position','Time-Before','Time-Starting']
            elif evn_type=='PersonnelEndPosition':
                role_all = ['trigger','Person','Entity','Time-Within','Place','Position','Time-Ending','Time-Holds','Defendant','Prosecutor']
            elif evn_type=='PersonnelNominate':
                role_all = ['trigger','Person','Agent','Time-Within','Position']
            elif evn_type=='PersonnelStartPosition':
                role_all = ['trigger','Person','Entity','Position','Place','Time-Within','Time-Starting','Time-Ending','Time-Holds','Time-Before','Time-After']
            elif evn_type=='TransactionTransferMoney':
                role_all = ['trigger','Giver','Money','Recipient','Place','Beneficiary','Time-Within','Time-Starting','Time-After','Time-At-Beginning','Time-Ending']
            elif evn_type=='TransactionTransferOwnership':
                role_all = ['trigger','Artifact','Buyer','Seller','Org','Time-Within','Place','Beneficiary','Price','Entity']

            for rol in role_all:  
                if rol not in role_lst:
                    n = str(random.randint(0, 7))
                    ids = ids+'_'+n
                    lst = []
                    word = ''
                    start_span = int(0)
                    end_span = int(0)
                    role = rol
                    all_lst = [ids,content,evn_type,word,start_span,role,end_span]
                    final_lst.append(all_lst)

                        
    return final_lst

def get_df():
    final_lst = change_data()
    df = pd.DataFrame()
    df = df.append(final_lst,ignore_index=True)
    df.columns = ['id','content','type','word','start_span','role']
    return df
        
        
def get_torch_mrc_all_train_data():
    final_lst = change_data()
    out_file = open('AI_RC/data/squad-like_all_train_data.json','w')
    lst = []
    dic1 = {}
    dic2 = {}
    for i in range(len(final_lst)):
        tmp_con = {}
        tmp_ans = {}
        tmp_pos = {}
        tmp_con['context'] = final_lst[i][1]
        tmp_pos['answer_start'] = int(final_lst[i][4])
        tmp_pos['answer_end'] = int(final_lst[i][6])
        text = final_lst[i][3]
        tmp_pos['text'] = text
        if text=='':
            tmp_pos['answer_type'] = "no-answer"
        else:
            tmp_pos['answer_type'] = "long-answer"
        tmp_ans['answers'] = [tmp_pos]
        tmp_con['qas'] = [tmp_ans]
        qus = final_lst[i][2]
        role = final_lst[i][5]
        con_qus = 'What is the role '+role+' of event type '+qus+' ?'
        tmp_ans['question'] = con_qus
        tmp_ans['id'] = final_lst[i][0]
        lst.append(tmp_con)
    dic1['title'] = 'ACE 2005 Event Extraction'
    dic1['paragraphs'] = lst
    dic2['data'] = [dic1]
    dic2['version'] = '1.1'
    data = json.dumps(dic2,ensure_ascii=False,indent=0)
    out_file.write(data)
    print('AI_RC模型的train集转换完成!')

def get_mrc_test_data():
    print('AI_RC模型的test集转换中...')
    cls_out = pd.read_csv('TC/test_output/cls_out.csv')
    test_data = pd.read_csv('TC/pybert/dataset/test.csv')
    all_cls_test_df = test_data.merge(cls_out, on='id')
    out_file = open('AI_RC/data/squad_like_test.json','w')
    lst = []
    dic1 = {}
    dic2 = {}
    for index,row in all_cls_test_df.iterrows():
        ids,content=row["id"],row["content"]
        # zy,gfgqzr,qs,tz,ggjc = row['zy'],row['gfgqzr'],row['qs'],row['tz'],row['ggjc'],
        Bankruptcy,EndOrg,MergeOrg,StartOrg,Attack,Demonstrate,Meet,PhoneWrite,Acquit,Appeal,Jail,Indict,Convict,Extradite,Fine,Pardon,Parole,Sentence,Sue,Hearing,Born,Die,Divorce,Injure,Marry,Transport,Elect,EndPosition,Nominate,StartPosition,Money,Ownership = row['Bankruptcy'],row['EndOrg'],row['MergeOrg'],row['StartOrg'],row['Attack'],row['Demonstrate'],row['Meet'],row['PhoneWrite'],row['Acquit'],row['Appeal'],row['Jail'],row['Indict'],row['Convict'],row['Extradite'],row['Fine'],row['Pardon'],row['Parole'],row['Sentence'],row['Sue'],row['Hearing'],row['Born'],row['Die'],row['Divorce'],row['Injure'],row['Marry'],row['Transport'],row['Elect'],row['EndPosition'],row['Nominate'],row['StartPosition'],row['Money'],row['Ownership'],
        #print(ids,content,zy,gfgqzr,qs,tz,ggjc)
        if Bankruptcy==1:
            ctype = 'BusinessDeclareBankruptcy'
            role_Bankruptcy = ['Org','Time-Within','trigger']
            for i in role_Bankruptcy:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if EndOrg==1:
            ctype = 'BusinessEndOrg'
            role_EndOrg = ['trigger','Org', 'Time-Within','Person','Place','Beneficiary']
            for i in role_EndOrg:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if MergeOrg==1:
            ctype = 'BusinessMergeOrg'
            role_MergeOrg = ['Org','Time-Starting','Place','trigger','Seller','Buyer','Time-Within','Time-Before','Time-Ending']
            for i in role_MergeOrg:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if StartOrg==1:
            ctype = 'BusinessStartOrg'
            role_StartOrg = ['Org','Agent','Time-Within','Place','Time-Starting','trigger','Time-Before','Time-After','Person','Destination']
            for i in role_StartOrg:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Attack==1:
            ctype = 'ConflictAttack'
            role_Attack = ['trigger','Place','Entity','Time-Within','Agent','Destination','Attacker','Time-Starting','Time-Ending','Victim','Person','Origin','Instrument','Time-Holds','Defendant','Target','Crime','Artifact','Time-Before','Vehicle','Org','Time-After','Adjudicator','Plaintiff','Sentence','Time-At-End','Time-At-Beginning','Position']
            for i in role_Attack:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)

        if Demonstrate==1:
            ctype = 'ConflictDemonstrate'
            role_Demonstrate = ['Place','Entity','Time-Within','trigger','Person','Time-Before','Attacker','Target','Time-Starting','Vehicle','Artifact','Destination','Origin','Time-Holds','Time-After']
            for i in role_Demonstrate:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Meet==1:
            ctype = 'ContactMeet'
            role_Meet = ['trigger','Entity','Time-Within','Place','Org','Agent','Time-Holds','Person','Destination','Defendant','Time-Ending','Time-Before','Time-After','Time-Starting']
            for i in role_Meet:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if PhoneWrite==1:
            ctype = 'ContactPhoneWrite'
            role_PhoneWrite = ['Entity','trigger','Time-Within','Adjudicator','Defendant','Crime','Place','Time-Before','Time-Starting']
            for i in role_PhoneWrite:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Acquit==1:
            ctype = 'JusticeAcquit'
            role_Acquit = ['trigger','Defendant','Crime','Adjudicator','Place']
            for i in role_Acquit:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Appeal==1:
            ctype = 'JusticeAppeal'
            role_Appeal = ['trigger','Plaintiff','Adjudicator','Time-Within','Person','Agent','Time-Starting','Defendant','Place','Time-Holds','Time-At-Beginning','Time-Before','Time-Ending','Giver','Money','Recipient']
            for i in role_Appeal:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Jail==1:
            ctype = 'JusticeArrestJail'
            role_Jail = ['trigger','Person','Agent','Place','Time-Within','Time-Holds','Time-Ending','Time-Starting','Destination','Time-Before','Crime','Defendant','Sentence','Entity','Position']
            for i in role_Jail:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Indict==1:
            ctype = 'JusticeChargeIndict'
            role_Indict = ['Defendant','Adjudicator','Time-Within','Prosecutor','Crime','trigger','Place','Time-After','Person','Destination']
            for i in role_Indict:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Convict==1:
            ctype = 'JusticeConvict'
            role_Convict = ['Defendant','Giver','Money','Place','trigger','Adjudicator','Time-Within','Crime','Time-After']
            for i in role_Convict:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Extradite==1:
            ctype = 'JusticeExtradite'
            role_Extradite = ['trigger','Person','Agent','Origin','Destination','Crime']
            for i in role_Extradite:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Fine==1:
            ctype = 'JusticeFine'
            role_Fine = ['trigger','Entity','Money','Adjudicator','Crime','Time-Within','Place']
            for i in role_Fine:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Pardon==1:
            ctype = 'JusticePardon'
            role_Pardon = ['Defendant','Adjudicator','Time-Within','trigger']
            for i in role_Pardon:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Parole==1:
            ctype = 'JusticeReleaseParole'
            role_Parole = ['Person','Place','Agent','Time-Within','trigger','Crime','Entity','Defendant','Adjudicator']
            for i in role_Parole:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Sentence==1:
            ctype = 'JusticeSentence'
            role_Sentence = ['trigger','Defendant','Sentence','Crime','Adjudicator','Time-Within','Plaintiff','Place','Time-After','Time-Holds','Org']
            for i in role_Sentence:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Sue==1:
            ctype = 'JusticeSue'
            role_Sue = ['Adjudicator','Defendant','trigger','Crime','Plaintiff','Time-Within','Place','Time-Starting','Person','Entity','Time-Ending']
            for i in role_Sue:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Hearing==1:
            ctype = 'JusticeTrialHearing'
            role_Hearing = ['Adjudicator','Defendant','Crime','Time-Starting','trigger','Time-Within','Time-At-End','Person','Entity','Time-Ending','Place','Time-At-Beginning','Agent','Sentence','Time-Holds','Plaintiff','Position','Org','Destination','Prosecutor','Time-Before']
            for i in role_Hearing:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Born==1:
            ctype = 'LifeBeBorn'
            role_Born = ['trigger','Person','Place','Time-Within','Agent','Origin']
            for i in role_Born:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Die==1:
            ctype = 'LifeDie'
            role_Die = ['Agent','Destination','trigger','Victim','Place','Time-Within','Time-After','Time-Before','Attacker','Target','Instrument','Time-Starting','Time-Holds','Entity','Time-Ending','Person','Origin']
            for i in role_Die:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Divorce==1:
            ctype = 'LifeDivorce'
            role_Divorce = ['trigger','Person']
            for i in role_Divorce:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Injure==1:
            ctype = 'LifeInjure'
            role_Injure = ['Adjudicator','Defendant','Place','Sentence','Crime','Time-Within','Instrument','Victim','Agent','Time-Holds','Time-Starting','trigger','Attacker','Target','Time-Ending']
            for i in role_Injure:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Marry==1:
            ctype = 'LifeMarry'
            role_Marry = ['Person','Place','Time-Within','trigger','Time-After','Time-Holds']
            for i in role_Marry:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)      
        if Transport==1:
            ctype = 'MovementTransport'
            role_Transport = ['trigger','Vehicle','Destination','Origin','Time-Before','Person','Time-Within','Time-Holds','Attacker','Target','Time-Ending','Time-After','Agent','Time-Starting','Artifact','Place','Position','Entity','Victim','Time-At-End','Time-At-End','Time-At-Beginning','Time-At-End','Time-At-End']
            for i in role_Transport:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Elect==1:
            ctype = 'PersonnelElect'
            role_Elect = ['trigger','Person','Place','Entity','Time-Within','Time-Holds','Adjudicator','Plaintiff','Position','Time-Before','Time-Starting']
            for i in role_Elect:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if EndPosition==1:
            ctype = 'PersonnelEndPosition'
            role_EndPosition = ['trigger','Person','Entity','Time-Within','Place','Position','Time-Ending','Time-Holds','Defendant','Prosecutor']
            for i in role_EndPosition:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Nominate==1:
            ctype = 'PersonnelNominate'
            role_Nominate = ['trigger','Person','Agent','Time-Within','Position']
            for i in role_Nominate:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if StartPosition==1:
            ctype = 'PersonnelStartPosition'
            role_StartPosition = ['trigger','Person','Entity','Position','Place','Time-Within','Time-Starting','Time-Ending','Time-Holds','Time-Before','Time-After']
            for i in role_StartPosition:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)      
        if Money==1:
            ctype = 'TransactionTransferMoney'
            role_Money = ['trigger','Giver','Money','Recipient','Place','Beneficiary','Time-Within','Time-Starting','Time-After','Time-At-Beginning','Time-Ending']
            for i in role_Money:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if Ownership==1:
            ctype = 'TransactionTransferOwnership'
            role_Ownership = ['trigger','Artifact','Buyer','Seller','Org','Time-Within','Place','Beneficiary','Price','Entity']
            for i in role_Ownership:
                n = str(random.randint(0, 7))
                ids = str(ids)+'_'+n
                tmp_con = {}
                tmp_ans = {}
                tmp_pos = {}
                tmp_con['context'] = content
                tmp_pos['answer_start'] = int(0)
                tmp_pos['answer_end'] = int(0)
                tmp_pos['text'] = ''
                tmp_pos['answer_type'] = ''
                tmp_ans['answers'] = [tmp_pos]
                tmp_con['qas'] = [tmp_ans]
                qus = ctype
                role = i
                con_qus = 'What is the role '+role+' of event type '+qus+' ?'
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)     

        if Bankruptcy==0 and EndOrg==0 and MergeOrg==0 and StartOrg==0 and Attack==0 and Demonstrate==0 and Meet==0 and PhoneWrite==0 and Acquit==0 and Appeal==0 and Jail==0 and Indict==0 and Convict==0 and Extradite==0 and Fine==0 and Pardon==0 and Parole==0 and Sentence==0 and Sue==0 and Hearing==0 and Born==0 and Die==0 and Divorce==0 and Injure==0 and Marry==0 and Transport==0 and Elect==0 and EndPosition==0 and Nominate==0 and StartPosition==0 and Money==0 and Ownership==0:
            ids = str(ids)
            #print(ids)
            tmp_con = {}
            tmp_ans = {}
            tmp_pos = {}
            tmp_con['context'] = content
            tmp_pos['answer_start'] = int(0)
            tmp_pos['answer_end'] = int(0)
            tmp_pos['text'] = ''
            tmp_pos['answer_type'] = ''
            tmp_ans['answers'] = [tmp_pos]
            tmp_con['qas'] = [tmp_ans]
            qus = ''
            role = ''
            con_qus = 'What is the role '+role+' of event type '+qus+' ?'
            tmp_ans['question'] = con_qus
            tmp_ans['id'] = ids
            lst.append(tmp_con)

    dic1['title'] =  'ACE 2005 Event Extraction'
    dic1['paragraphs'] = lst
    dic2['data'] = [dic1]
    dic2['version'] = '1.1'
    data = json.dumps(dic2,ensure_ascii=False,indent=0)
    out_file.write(data)
    print('AI_RC模型的test集转换完成!')    
if __name__ == '__main__':
    get_torch_mrc_all_train_data()
    get_mrc_test_data()
