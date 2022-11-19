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
        on tb_correntista.cod_correntista = tb_movimentacao.cod_correntista

SEL