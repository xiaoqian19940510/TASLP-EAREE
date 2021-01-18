import torch.nn as nn
import torch
from pytorch_pretrained_bert.modeling import BertPreTrainedModel, BertModel
from net.Gatlayer import GAT

class QaExtract(BertPreTrainedModel):
    def __init__(self, config):
        super(QaExtract, self).__init__(config)
        self.bert = BertModel(config)
        # for p in self.bert.parameters():
        #     p.requires_grad = False
        #config.nfeature,config.gat_nhidden,config.num_labels,config.hidden_dropout_prob,\
        #    config.gat_alpha,config.gat_nhead,config.gat_layer
        self.GAT = GAT(config.hidden_size,30,30,0.5,0.1,3,2)

        self.start_end_fc = nn.Linear(config.hidden_size + 30, config.hidden_size, bias=False)
        # nn.init.xavier_uniform_(self.start_end_fc.weight, gain=1.414)

        self.logit_fc = nn.Linear(config.hidden_size + 30, config.hidden_size, bias=False)
        # nn.init.xavier_uniform_(self.logit_fc.weight, gain=1.414)

        self.classifier = nn.Linear(config.hidden_size, 2)
        self.apply(self.init_bert_weights)
        self.answer_type_classifier = nn.Linear(config.hidden_size, 4)

    def forward(self, input_ids, adj,token_type_ids, attention_mask, output_all_encoded_layers=False):
        sequence_output, pooled_output = self.bert(input_ids,
                                                   token_type_ids,
                                                    attention_mask,
                                                    output_all_encoded_layers=output_all_encoded_layers)  # (B, T, 768)
        # print(sequence_output.shape)
        # print(pooled_output.shape)
        # print(adj.shape)
        Gat_outputs = self.GAT(sequence_output,adj[:,0,:,:])
        sequence_output = self.start_end_fc( torch.cat( (sequence_output,Gat_outputs),2))

        logits = self.classifier(sequence_output)                                          # (B, T, 2)
        start_logits, end_logits = logits.split(1, dim=-1)                                 # ((B, T, 1), (B, T, 1))
        start_logits = start_logits.squeeze(-1)                                            # (B, T)
        end_logits = end_logits.squeeze(-1)                                                # (B, T)
        
        pooled_output = self.logit_fc( torch.cat( (pooled_output,Gat_outputs[:,0,:]),1))
        answer_type_logits = self.answer_type_classifier(pooled_output)
        return start_logits, end_logits, answer_type_logits