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
