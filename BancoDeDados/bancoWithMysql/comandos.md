create definer = gustavo@localhost view bancosa.vw_extratoCorrentista as
select `bancosa`.`tb_correntista`.`cod_correntista`     AS `cod_correntista`,
       `bancosa`.`tb_correntista`.`nome_correntista`    AS `nome_correntista`,
       `bancosa`.`tb_movimentacao`.`data_operacao`      AS `data_operacao`,
       `bancosa`.`tb_movimentacao`.`tipo_transacao`     AS `tipo_transacao`,
       `bancosa`.`tb_movimentacao`.`valor_movimentacao` AS `valor_movimentacao`,
       (case `bancosa`.`tb_movimentacao`.`tipo_transacao`
            when 'DP' then 'Deposito'
            when 'SQ' then 'Saque'
            when 'PG' then 'Pagamento'
            when 'TC' then 'Transferencia de crédito'
            when 'TD' then 'Transferencia de debito' end)  AS `tipo_Operacao_Descricao`
from (`bancosa`.`tb_correntista` join `bancosa`.`tb_movimentacao`
      on ((`bancosa`.`tb_correntista`.`cod_correntista` = `bancosa`.`tb_movimentacao`.`cod_correntista`)));
create
    definer = gustavo@localhost procedure bancosa.sp_deposito(IN sp_cod_correntista int, IN sp_valor float)
begin
    insert into tb_movimentacao(cod_correntista, tipo_transacao, valor_movimentacao, data_operacao)
        values (sp_cod_correntista, 'DP',sp_valor, NOW());
end;

create
    definer = gustavo@localhost procedure bancosa.sp_extrato_correntista(IN sp_cod_correntista int,
                                                                            IN sp_data_inicial datetime,
                                                                            IN sp_data_final datetime)
begin
    select data_operacao, tipo_transacao,valor_movimentacao from vw_extratoCorrentista
        where cod_correntista=sp_cod_correntista
        and data_operacao between sp_data_inicial and sp_data_final
        order by data_operacao;
end;
create
    definer = gustavo@localhost procedure bancosa.sp_pagamento(IN sp_cod_correntista_pagamento int, IN sp_valor_pagamento float)
begin
    insert into tb_movimentacao(cod_correntista, tipo_transacao, valor_movimentacao, data_operacao)
        values (sp_cod_correntista_pagamento, 'PG', sp_valor_pagamento, now());
end;
create
    definer = gustavo@localhost procedure sp_saque(IN sp_cod_saque int, IN sp_valor_saque float)
begin
    insert into tb_movimentacao(cod_correntista, tipo_transacao, valor_movimentacao, data_operacao)
        values (sp_cod_saque,'SQ',sp_valor_saque, NOW());
end;
create
    definer = gustavo@localhost procedure bancosa.sp_transferencia(IN sp_cod_transf_origem int,
                                                                      IN sp_cod_transf_destino int,
                                                                      IN sp_valor_transferencia float)
begin
    insert into tb_movimentacao(cod_correntista,tipo_transacao,valor_movimentacao,data_operacao)
        values (sp_cod_transf_origem, 'TD',sp_valor_transferencia, NOW());
    IF  (@@ERROR_COUNT = 0 )
    then
        INSERT INTO tb_movimentacao(cod_correntista, tipo_transacao, valor_movimentacao, data_operacao)
        values (sp_cod_transf_destino,'TC',sp_valor_transferencia,NOW());
    end if;
end;
use bancosa;
create trigger ti_movimentacao after insert
    on tb_movimentacao for each row
    begin
        DECLARE codigo_correntista int;
        DECLARE valor float(10,2);
        DECLARE tipo_transacao char(2);

       select m.cod_correntista, m.valor_movimentacao, m.tipo_transacao into codigo_correntista, valor, tipo_transacao from tb_movimentacao as m;
        if tipo_transacao in ('TC', 'DP') then
            update tb_correntista set saldo_correntista= NEW.valor_movimentacao + valor where cod_correntista = new.cod_correntista;
        else
            update tb_correntista set saldo_correntista= new.valor_movimentacao + valor where cod_correntista = new.cod_correntista;
        end if;
    end;







