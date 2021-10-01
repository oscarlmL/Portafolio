# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    rut_adm = models.TextField(primary_key=True)  # This field type is a guess.
    pass_field = models.TextField(db_column='pass')  # Field renamed because it was a Python reserved word. This field type is a guess.
    nombre_adm = models.TextField()  # This field type is a guess.
    apat_adm = models.TextField()  # This field type is a guess.
    amat_adm = models.TextField()  # This field type is a guess.
    email_admin = models.TextField()  # This field type is a guess.
    fono_admin = models.BigIntegerField()
    restaurant_id_restaurante = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='restaurant_id_restaurante')

    class Meta:
        managed = False
        db_table = 'administrador'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cajero(models.Model):
    id_cajero = models.BigIntegerField(primary_key=True)
    nom_cajero = models.TextField()  # This field type is a guess.
    restaurant_id_restaurante = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='restaurant_id_restaurante')

    class Meta:
        managed = False
        db_table = 'cajero'


class Carta(models.Model):
    tipo_plato = models.TextField()  # This field type is a guess.
    estilo_comida = models.TextField()  # This field type is a guess.
    restaurant_id_restaurante = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='restaurant_id_restaurante', primary_key=True)
    plato_id_plato = models.ForeignKey('Plato', models.DO_NOTHING, db_column='plato_id_plato')
    enc_cocina_id_enc_cocina = models.ForeignKey('EncCocina', models.DO_NOTHING, db_column='enc_cocina_id_enc_cocina')

    class Meta:
        managed = False
        db_table = 'carta'
        unique_together = (('restaurant_id_restaurante', 'plato_id_plato'),)


class Cliente(models.Model):
    rut_cli = models.TextField(primary_key=True)  # This field type is a guess.
    nombre_cli = models.TextField()  # This field type is a guess.
    apaterno_cli = models.TextField()  # This field type is a guess.
    amaterno_cli = models.TextField()  # This field type is a guess.
    fono_cli = models.BigIntegerField()
    email_cli = models.TextField()  # This field type is a guess.
    saldo_cli = models.BigIntegerField()
    pass_field = models.TextField(db_column='pass')  # Field renamed because it was a Python reserved word. This field type is a guess.
    direccion_cliente = models.TextField()  # This field type is a guess.
    convenio = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cliente'


class Convenio(models.Model):
    rut_cli = models.TextField()  # This field type is a guess.
    nom_cli = models.TextField()  # This field type is a guess.
    nom_emp = models.TextField()  # This field type is a guess.
    rut_emp = models.TextField()  # This field type is a guess.
    tipo_suscrip = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'convenio'


class DetPago(models.Model):
    precio_unidad = models.BigIntegerField()
    total = models.BigIntegerField()
    direccion_entrega = models.TextField()  # This field type is a guess.
    pago_id_pago = models.ForeignKey('Pago', models.DO_NOTHING, db_column='pago_id_pago', primary_key=True)
    pedido_id_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='pedido_id_pedido')
    repartidor_id_repartidor = models.ForeignKey('Repartidor', models.DO_NOTHING, db_column='repartidor_id_repartidor')

    class Meta:
        managed = False
        db_table = 'det_pago'
        unique_together = (('pago_id_pago', 'pedido_id_pedido'),)


class DetalleInsumos(models.Model):
    id_det_ins = models.BigIntegerField(primary_key=True)
    desc_det_ins = models.TextField()  # This field type is a guess.
    valor_ing = models.BigIntegerField()
    ingrediente_id_ing = models.ForeignKey('Ingrediente', models.DO_NOTHING, db_column='ingrediente_id_ing')
    proveedor_id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_id_proveedor')

    class Meta:
        managed = False
        db_table = 'detalle_insumos'
        unique_together = (('id_det_ins', 'ingrediente_id_ing', 'proveedor_id_proveedor'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    rut_emp = models.TextField(primary_key=True)  # This field type is a guess.
    nom_emp = models.TextField()  # This field type is a guess.
    nom_gerente = models.TextField()  # This field type is a guess.
    cant_trabajadores = models.BigIntegerField()
    enc_convenio_id_enc_conv = models.ForeignKey('EncConvenio', models.DO_NOTHING, db_column='enc_convenio_id_enc_conv')

    class Meta:
        managed = False
        db_table = 'empresa'


class EncCocina(models.Model):
    id_enc_cocina = models.AutoField(primary_key=True)
    nom_enc_cocina = models.CharField(max_length=100)  # This field type is a guess.
    titulo = models.CharField(max_length=100)  # This field type is a guess.
    exp_laboral = models.IntegerField()
    email_enc_cocina = models.EmailField() # This field type is a guess.
    contraseña1 = models.CharField(max_length=100)
    contraseña2 = models.CharField(max_length=100)

    class Meta:
        db_table = 'enc_cocina'


class EncConvenio(models.Model):
    id_enc_conv = models.AutoField(primary_key=True)
    rut_enc_conv = models.CharField(max_length=100)  # This field type is a guess.
    nom_enc_conv = models.CharField(max_length=100)  # This field type is a guess.
    ap_enc_conv = models.CharField(max_length=100)  # This field type is a guess.
    email_enc_conv = models.EmailField()  # This field type is a guess.
    contraseña1 = models.CharField(max_length=100)
    contraseña2 = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'enc_convenio'


class Informes(models.Model):
    id_pedido = models.BigIntegerField()
    id_plato = models.BigIntegerField()
    fec_pedido = models.TextField()  # This field type is a guess.
    total_pedido = models.BigIntegerField()
    nom_plato = models.TextField()  # This field type is a guess.
    nom_ing = models.TextField()  # This field type is a guess.
    valor_ing = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'informes'


class Ingrediente(models.Model):
    id_ing = models.BigIntegerField(primary_key=True)
    nom_ing = models.TextField()  # This field type is a guess.
    desc_ing = models.TextField()  # This field type is a guess.
    tipo_ing = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ingrediente'


class Pago(models.Model):
    id_pago = models.BigIntegerField(primary_key=True)
    tipo_pago = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pago'


class Pedido(models.Model):
    id_pedido = models.BigIntegerField(primary_key=True)
    estado = models.TextField()  # This field type is a guess.
    fecha_pedido = models.TextField()  # This field type is a guess.
    cliente_rut_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_rut_cli')
    restaurant_id_restaurante = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='restaurant_id_restaurante')

    class Meta:
        managed = False
        db_table = 'pedido'


class Plato(models.Model):
    id_plato = models.BigIntegerField(primary_key=True)
    nom_plato = models.TextField()  # This field type is a guess.
    valor_plato = models.BigIntegerField()
    descripcion = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'plato'


class Preparacin(models.Model):
    id_prepa = models.BigIntegerField(primary_key=True)
    desc_preparacion = models.TextField()  # This field type is a guess.
    plato_id_plato = models.ForeignKey(Plato, models.DO_NOTHING, db_column='plato_id_plato')
    ingrediente_id_ing = models.ForeignKey(Ingrediente, models.DO_NOTHING, db_column='ingrediente_id_ing')
    lista_ing = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'preparación'
        unique_together = (('id_prepa', 'plato_id_plato', 'ingrediente_id_ing'),)


class Proveedor(models.Model):
    id_proveedor = models.BigIntegerField(primary_key=True)
    rol_local = models.TextField()  # This field type is a guess.
    nom_proveedor = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'proveedor'


class Repartidor(models.Model):
    id_repartidor = models.BigIntegerField(primary_key=True)
    nombre_repartidor = models.TextField()  # This field type is a guess.
    apellido_repartidor = models.TextField()  # This field type is a guess.
    patente_veh = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'repartidor'


class Restaurant(models.Model):
    id_restaurante = models.BigIntegerField(primary_key=True)
    nombre_rest = models.TextField()  # This field type is a guess.
    direccion_rest = models.TextField()  # This field type is a guess.
    comuna_rest = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'restaurant'


class Suscripcin(models.Model):
    id_suscrip = models.BigIntegerField(primary_key=True)
    tipo_suscrip = models.TextField()  # This field type is a guess.
    desc_suscrip = models.TextField()  # This field type is a guess.
    administrador_rut_adm = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador_rut_adm')
    enc_convenio_id_enc_conv = models.ForeignKey(EncConvenio, models.DO_NOTHING, db_column='enc_convenio_id_enc_conv')

    class Meta:
        managed = False
        db_table = 'suscripción'
