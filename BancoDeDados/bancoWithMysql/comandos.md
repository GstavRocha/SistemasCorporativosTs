create table tb_correntista(
    cod_correntista int(10) not null  auto_increment,
    nome_correntista varchar(60) not null,
    email_correntista varchar(50) not null,
    saldo_correntista float(10,2) not null,
    constraint pk_correntista primary key (cod_correntista)
);
alter table tb_correntista add constraint  chk_condicao check (saldo_correntista >= 0 );

create table tb_movimentacao(
    cod_movimentacao int(10) not null  auto_increment,
    cod_correntista int(10) not null,
    tipo_transacao char(2) not null,
    valor_movimentacao  float(10,2) not null,
    data_operacao datetime not null,
    constraint pk_movimentacao primary key (cod_movimentacao),
    constraint chk_mov_cond check ( valor_movimentacao > 0)
);

alter table tb_movimentacao add constraint fk_cod_correntista foreign key (cod_correntista) references tb_correntista(cod_correntista);

DELETE FROM tb_correntista WHERE cod_correntista=3;

ALTER TABLE tb_movimentacao add data_operacao TIMESTAMP NOT NULL  DEFAULT  CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP; # Setando data automatica

alter table tb_movimentacao drop data_operacao;

insert into tb_movimentacao(cod_correntista,tipo_transacao,valor_movimentacao)
values (03,'ts',100.2);
DELETE FROM tb_movimentacao WHERE cod_movimentacao = 1;

create view vw_extratoCorrentista
as
    select tb_correntista.cod_correntista,
           tb_correntista.nome_correntista,
           tb_movimentacao.data_operacao,
           tb_movimentacao.tipo_transacao,
           tb_movimentacao.valor_movimentacao,
           CASE tb_movimentacao.tipo_transacao
                when  'DP' then 'Deposito'
                When 'SQ' then 'Saque'
                When 'PG' then 'Pagamento'
                when 'TC' then 'Transferencia de crédito'
                when 'TD' then 'Transferencia de debito'
            END as tipo_Operacao_Descricao
    FROM tb_correntista inner join tb_movimentacao
        on tb_correntista.cod_correntista = tb_movimentacao.cod_correntista;

insert into  tb_correntista(cod_correntista, nome_correntista, email_correntista, saldo_correntista) VALUES (1,'Gustavo','gustavo@email',0)
create
    definer = gustavo@localhost procedure sp_deposito(IN sp_cod_correntista int, IN sp_valor float)
begin
    insert into tb_movimentacao(cod_correntista, tipo_transacao, valor_movimentacao, data_operacao)
        values (sp_cod_correntista, 'DP',sp_valor, NOW());
end;

create
    definer =gustavo@localhost procedure sp_extrato_correntista(in sp_cod_correntista int , in sp_data_inicial datetime , in sp_data_final datetime )
begin
    select data_operacao, tipo_transacao,valor_movimentacao from vw_extratoCorrentista
        where cod_correntista=sp_cod_correntista
        and data_operacao between sp_data_inicial and sp_data_final
        order by data_operacao;
end;
call sp_extrato_correntista(1,'2022-12-01 15:58:06','2022-12-01 17:16:06');
create
    definer =gustavo@localhost procedure sp_pagamento(in sp_cod_correntista_pagamento int, in sp_valor_pagamento float)
begin
    insert into tb_movimentacao(cod_correntista, tipo_transacao, valor_movimentacao, data_operacao)
        values (sp_cod_correntista_pagamento, 'PG', sp_valor_pagamento, now());
end;
create
    definer =gustavo@localhost procedure sp_saque(in sp_cod_saque int, in sp_valor_saque float)
begin
    insert into tb_movimentacao(cod_correntista, tipo_transacao, valor_movimentacao, data_operacao)
        values (sp_cod_saque,'SQ',sp_valor_saque, NOW());
end;
create
    definer =gustavo@localhost procedure sp_transferencia(in sp_cod_transf_origem int,in sp_cod_transf_destino int, sp_valor_transferencia float)
begin
    insert into tb_movimentacao(cod_correntista,tipo_transacao,valor_movimentacao,data_operacao)
        values (sp_cod_transf_origem, 'TD',sp_valor_transferencia, NOW());
    IF  (@@ERROR_COUNT = 0 )
    then
        INSERT INTO tb_movimentacao(cod_correntista, tipo_transacao, valor_movimentacao, data_operacao)
        values (sp_cod_transf_destino,'TC',sp_valor_transferencia,NOW());
    end if;
end;

create trigger ti_movimentacoes AFTER insert
    on tb_movimentacao
for each row
    begin
        declare ti_cod_correntista int;
        declare ti_valor float;
        declare ti_tipo_transacao VARCHAR(2);

        set ti_cod_correntista = new.tipo_transacao;
        set ti_valor = new.valor_movimentacao;
        set ti_tipo_transacao = new.tipo_transacao;
        from inserted;
    end;
