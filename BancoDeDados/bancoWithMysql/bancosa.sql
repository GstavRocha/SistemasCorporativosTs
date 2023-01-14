create table tb_correntista
(
    cod_correntista   int auto_increment
        primary key,
    nome_correntista  varchar(60)  not null,
    email_correntista varchar(50)  not null,
    saldo_correntista float(10, 2) not null,
    constraint chk_condicao
        check (`saldo_correntista` >= 0)
);

create table tb_movimentacao
(
    cod_movimentacao   int auto_increment
        primary key,
    cod_correntista    int                                 not null,
    tipo_movimentacao  char(2)                             not null,
    valor_movimentacao float(10, 2)                        not null,
    data_movimentacao  timestamp default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    constraint fk_movimentacao_correntista
        foreign key (cod_correntista) references tb_correntista (cod_correntista)
);

create definer = gustavo@localhost view vw_extratoCorrentista as
select `bancosa`.`tb_correntista`.`cod_correntista`       AS `cod_correntista`,
       `bancosa`.`tb_correntista`.`nome_correntista`      AS `nome_correntista`,
       `bancosa`.`tb_movimentacao`.`data_movimentacao`    AS `data_operacao`,
       `bancosa`.`tb_movimentacao`.`tipo_movimentacao`    AS `tipo_transacao`,
       `bancosa`.`tb_movimentacao`.`valor_movimentacao`   AS `valor_movimentacao`,
       (case `bancosa`.`tb_movimentacao`.`tipo_movimentacao`
            when 'DP' then 'Deposito'
            when 'SQ' then 'Saque'
            when 'PG' then 'Pagamento'
            when 'TC' then 'Transferencia de crédito'
            when 'TD' then 'Transferencia de debito' end) AS `tipo_Operacao_Descricao`
from (`bancosa`.`tb_correntista` join `bancosa`.`tb_movimentacao`
      on ((`bancosa`.`tb_correntista`.`cod_correntista` = `bancosa`.`tb_movimentacao`.`cod_correntista`)));

create
    definer = gustavo@localhost procedure sp_deposito(IN sp_cod_correntista int, IN sp_valor float)
begin
    insert into tb_movimentacao(cod_correntista, tipo_movimentacao, valor_movimentacao, data_movimentacao)
        values (sp_cod_correntista, 'DP',sp_valor, NOW());
end;

create
    definer = gustavo@localhost procedure sp_extrato_correntista(IN sp_cod_correntista int, IN sp_data_inicial datetime,
                                                                 IN sp_data_final datetime)
begin
    select data_movimentacao, tipo_movimentacao,valor_movimentacao from tb_movimentacao
        where cod_correntista=sp_cod_correntista
        and data_movimentacao between sp_data_inicial and sp_data_final
        order by data_movimentacao;
end;

create
    definer = gustavo@localhost procedure sp_pagamento(IN sp_cod_correntista_pagamento int, IN sp_valor_pagamento float)
begin
    insert into tb_movimentacao(cod_correntista, tipo_movimentacao, valor_movimentacao, data_movimentacao)
        values (sp_cod_correntista_pagamento, 'PG', sp_valor_pagamento, now());
end;

create
    definer = gustavo@localhost procedure sp_saque(IN sp_cod_saque int, IN sp_valor_saque float)
begin
    insert into tb_movimentacao(cod_correntista, tipo_movimentacao, valor_movimentacao, data_movimentacao)
        values (sp_cod_saque,'SQ',sp_valor_saque, NOW());
end;

create
    definer = gustavo@localhost procedure sp_transferencia(IN sp_cod_transf_origem int, IN sp_cod_transf_destino int,
                                                           IN sp_valor_transferencia float)
begin
    insert into tb_movimentacao(cod_correntista,tipo_movimentacao,valor_movimentacao,data_movimentacao)
        values (sp_cod_transf_origem, 'TD',sp_valor_transferencia, NOW());
    IF  (@@ERROR_COUNT = 0 )
    then
        INSERT INTO tb_movimentacao(cod_correntista, tipo_movimentacao, valor_movimentacao, data_movimentacao)
        values (sp_cod_transf_destino,'TC',sp_valor_transferencia,NOW());
    end if;
end;


