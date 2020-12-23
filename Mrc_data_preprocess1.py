import json
import pandas as pd
import random


def change_data():
    in_file = open('/home/LAB/liqian/test/game/Ori_graph/dataset/train_base.json','r')
    final_lst = []
    for line in in_file:
        line = line.strip()
        line = json.loads(line)
        ids = str(line['id'])
        content = line['content']
        for k in line['events']:
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
            if evn_type=='质押':
                role_all = ['trigger','sub-org','sub-per','obj-org','obj-per','collateral','date','money','number','proportion']
            elif evn_type=='股份股权转让':
                role_all = ['trigger','sub-org','sub-per','obj-org','obj-per','collateral','date','money','number','proportion','target-company']
            elif evn_type=='起诉':
                role_all = ['trigger','sub-org','sub-per','obj-org','obj-per','date']
            elif evn_type=='投资':
                role_all = ['trigger','sub','obj','money','date']
            elif evn_type=='减持':
                role_all = ['trigger','sub','obj','title','date','share-per','share-org']
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
    #df.to_csv('mrc_middle_data.csv',index=0)
    return df
        
        
def get_torch_mrc_all_train_data():
    final_lst = change_data()
    out_file = open('/home/LAB/liqian/test/game/Ori_graph/CCKS-Mrc/data/squad-like_all_train_data.json','w')
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
        Ori_type={'质押':'是债务人或第三方将其动产或权利移交债权人占有，将该动产或权利作为债权的担保。','股份股权转让':'是公司股东依法将自己的股东权益有偿转让给他人。','起诉':'依法向法院提出诉讼，请求法院对特定案件进行审判的行为。','投资':'是国家或企业以及个人，为了特定目的，与对方签订协议，促进社会发展，实现互惠互利，输送资金的过程。','减持':'是上市公司的高管在二级市场卖出自己公司股票的行为。'}
        chineseMean={'质押':{'trigger':'是触发词','sub-org':'是质押公司：发起质押的公司','sub-per':'是质押人：发起质押的个人','obj-org':'是质权公司：接受质押的公司','obj-per':'是质权人：接受质押的个人','collateral':'是质押物（标的，可为公司股票、大额存单等等）','date':'是质押日期','money':'是质押金额','number':'是质押数量','proportion':'是质押比例'},'股份股权转让':{'trigger':'是触发词','sub-org':'是股份股权转让公司：发起股份股权转让的公司','sub-per':'是股份股权转让人：发起股份股权转让的个人','obj-org':'是受转让公司：接受股份股权转让的公司','obj-per':'是受转让人：接受股份股权转让的个人','collateral':'是股份股权转让物（标的，可为公司股票、股权等等）','date':'是日期','money':'是转让交易金额','number':'是转让数量','proportion':'是转让比例','target-company':'是标的公司：指收购行为中的收购对象公司'},'起诉':{'trigger':'是触发词','sub-org':'是原告（公司）','sub-per':'是原告（个人）','obj-org':'是被告（公司）','obj-per':'是被告（个人）','date':'是日期'},'投资':{'trigger':'是触发词','sub':'是发起投资的组织或单位（投资方）','obj':'是被投资的组织或单位（被投资方）','money':'是投资金额','date':'是日期'},'减持':{'trigger':'是触发词','sub':'是减持方（通常为人，少数情况为组织）','obj':'是被减持方','title':'是减持方的职务','date':'是日期','share-per':'是减持的股份占个人股份百分比','share-org':'是减持的股份占公司股份的百分比'}}
        role = final_lst[i][5]
        con_qus = '事件类型为'+qus+'的'+role+'是什么？'+qus+Ori_type[qus]+role+chineseMean[qus][role]
        # con_qus = '事件类型为'+qus+'的'+role+'是什么？'+qus+'是上市公司的高管在二级市场卖出自己公司股票的行为。'+role+chinese[index]
        tmp_ans['question'] = con_qus
        tmp_ans['id'] = final_lst[i][0]
        lst.append(tmp_con)
    dic1['title'] = '小样本金融元素抽取'
    dic1['paragraphs'] = lst
    dic2['data'] = [dic1]
    dic2['version'] = '1.1'
    data = json.dumps(dic2,ensure_ascii=False,indent=0)
    out_file.write(data)
    print('Mrc模型的train集转换完成!')

def get_mrc_test_data():
    print('Mrc模型的test集转换中...')
    cls_out = pd.read_csv('/home/LAB/liqian/test/game/Ori_graph/CCKS-Cls/test_output/cls_out.csv')
    test_data = pd.read_csv('/home/LAB/liqian/test/game/Ori_graph/CCKS-Cls/pybert/dataset/test.csv')
    all_cls_test_df = test_data.merge(cls_out, on='id')
    out_file = open('CCKS-Mrc/data/squad_like_test.json','w')
    lst = []
    dic1 = {}
    dic2 = {}
    for index,row in all_cls_test_df.iterrows():
        ids,content=row["id"],row["content"]
        zy,gfgqzr,qs,tz,ggjc = row['zy'],row['gfgqzr'],row['qs'],row['tz'],row['ggjc'],
        #print(ids,content,zy,gfgqzr,qs,tz,ggjc)
        if zy==1:
            index=-1
            ctype = '质押'
            role_zy = ['trigger','sub-org','sub-per','obj-org','obj-per','collateral','date','money','number','proportion']
            chinese=['是触发词','是质押公司：发起质押的公司','是质押人：发起质押的个人','是质权公司：接受质押的公司','是质权人：接受质押的个人','是质押物（标的，可为公司股票、大额存单等等）','是质押日期','是质押金额','是质押数量','是质押比例']
            for i in role_zy:
                index=index+1
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
                con_qus = '事件类型为'+qus+'的'+role+'是什么？'+qus+'是债务人或第三方将其动产或权利移交债权人占有，将该动产或权利作为债权的担保。'+role+chinese[index]
                # con_qus = '事件类型为'+qus+'的'+role+'是什么？'+qus+'是上市公司的高管在二级市场卖出自己公司股票的行为。'+role+chinese[index]
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if gfgqzr==1:
            index=-1
            ctype = '股份股权转让'
            role_gfgqzr = ['trigger','sub-org','sub-per','obj-org','obj-per','collateral','date','money','number','proportion','target-company']
            chinese=['是触发词','是股份股权转让公司：发起股份股权转让的公司','是股份股权转让人：发起股份股权转让的个人','是受转让公司：接受股份股权转让的公司','是受转让人：接受股份股权转让的个人','是股份股权转让物（标的，可为公司股票、股权等等）','是日期','是转让交易金额','是转让数量','是转让比例','是标的公司：指收购行为中的收购对象公司']
            for i in role_gfgqzr:
                index=index+1
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
                con_qus = '事件类型为'+qus+'的'+role+'是什么？'+qus+'是公司股东依法将自己的股东权益有偿转让给他人。'+role+chinese[index]
                # con_qus = '事件类型为'+qus+'的'+role+'是什么？'+qus+'是上市公司的高管在二级市场卖出自己公司股票的行为。'+role+chinese[index]
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if qs==1:
            ctype = '起诉'
            index=-1
            role_qs = ['trigger','sub-org','sub-per','obj-org','obj-per','date']
            chinese=['是触发词','是原告（公司）','是原告（个人）','是被告（公司）','是被告（个人）','是日期']
            for i in role_qs:
                index=index+1
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
                con_qus = '事件类型为'+qus+'的'+role+'是什么？'+qus+'是依法向法院提出诉讼，请求法院对特定案件进行审判的行为。'+role+chinese[index]
                # con_qus = '事件类型为'+qus+'的'+role+'是什么？'+qus+'是上市公司的高管在二级市场卖出自己公司股票的行为。'+role+chinese[index]
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if tz==1:
            ctype = '投资'
            index=-1
            role_tz = ['trigger','sub','obj','money','date']
            chinese=['是触发词','是发起投资的组织或单位（投资方）','是被投资的组织或单位（被投资方）','是投资金额','是日期']
            for i in role_tz:
                index=index+1
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
                con_qus = '事件类型为'+qus+'的'+role+'是什么？'+qus+'是国家或企业以及个人，为了特定目的，与对方签订协议，促进社会发展，实现互惠互利，输送资金的过程。'+role+chinese[index]
                # con_qus = '事件类型为'+qus+'的'+role+'是什么？'+qus+'是上市公司的高管在二级市场卖出自己公司股票的行为。'+role+chinese[index]
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if ggjc==1:
            ctype = '减持'
            index=-1
            role_ggjc = ['trigger','sub','obj','title','date','share-per','share-org']
            chinese=['是触发词','是减持方（通常为人，少数情况为组织）','是被减持方','是减持方的职务','是日期','是减持的股份占个人股份百分比','是减持的股份占公司股份的百分比']
            for i in role_ggjc:
                index=index+1
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
                con_qus = '事件类型为'+qus+'的'+role+'是什么？'+qus+'是上市公司的高管在二级市场卖出自己公司股票的行为。'+role+chinese[index]
                tmp_ans['question'] = con_qus
                tmp_ans['id'] = ids
                lst.append(tmp_con)
        if zy==0 and gfgqzr==0 and qs==0 and tz==0 and ggjc==0:
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
            con_qus = '事件类型为'+qus+'的'+role+'是什么？'
            tmp_ans['question'] = con_qus
            tmp_ans['id'] = ids
            lst.append(tmp_con)

    dic1['title'] = '小样本金融元素抽取'
    dic1['paragraphs'] = lst
    dic2['data'] = [dic1]
    dic2['version'] = '1.1'
    data = json.dumps(dic2,ensure_ascii=False,indent=0)
    out_file.write(data)
    print('Mrc模型的test集转换完成!')    
if __name__ == '__main__':
    get_torch_mrc_all_train_data()
    get_mrc_test_data()
