from datetime import datetime
from typing import Sized
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,types,Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from Database.Base import Base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.schema import FetchedValue

class Hospital(Base):
    __tablename__ = "hospital"
    id_hospital = Column(Integer, primary_key=True, index=True)
    nombre = Column(String,nullable=False)
    direccion = Column(String,nullable=False)
    telefono = Column(String,nullable=False)
    estancias = relationship("Estancia",back_populates="hospital")

    hospital_procedimiento = relationship("HospitalProcedimiento",back_populates="hospital")


class Paciente(Base):
    __tablename__ = "paciente"
    id_paciente = Column(Integer,primary_key=True,index=True)
    identificador = Column(String,unique=True)
    nombre = Column(String,nullable=False)
    apellido_1 = Column(String,nullable=False)
    apellido_2 = Column(String,nullable=True)
    estancias = relationship("Estancia",back_populates="paciente")



class Estancia(Base):
    __tablename__ = "estancia"
    id_estancia = Column(Integer, primary_key=True, index=True)
    fecha_ingreso = Column(types.DateTime,default=datetime.now())
    identificador = Column(String,nullable=False,unique=True)
    id_paciente = Column(Integer,ForeignKey("paciente.id_paciente"))
    id_hospital = Column(Integer,ForeignKey("hospital.id_hospital"))
    hospital = relationship("Hospital",back_populates="estancias",cascade="all, delete")
    paciente = relationship("Paciente",back_populates="estancias",cascade="all, delete")
    responsable_estancia = relationship("ResponsableEstancia",back_populates="estancia")
    informes = relationship("Informe",back_populates="estancia",order_by="desc(Informe.fecha)")
    procedimiento_autorizacion = relationship("ProcedimientoAutorizacion",back_populates="estancia")
    re = association_proxy('responsable_estancia', 'responsable')

    def __repr__(self) -> str:
        return f"Estancia:{self.id_estancia}, fecha_ingreso:{self.fecha_ingreso}, hospital: {self.id_hospital}"

class Responsable(Base):
    __tablename__ = "responsable"
    id_responsable = Column(Integer,primary_key=True,index=True)
    identificador = Column(String,unique=True)
    nombre = Column(String,nullable=False)
    apellido_1 = Column(String,nullable=False)
    apellido_2 = Column(String,nullable=True)
    email = Column(String,unique=True)
    password = Column(String,nullable=False)
    dispositivos = relationship("DispositivoResposable",back_populates="responsable")
    responsable_estancia = relationship("ResponsableEstancia",back_populates="responsable")
    notificaciones = relationship("Notificacion",back_populates="responsable")
    procedimiento_autorizacion = relationship("ProcedimientoAutorizacion",back_populates="responsable")
    tokens = relationship("AuthResponsableToken",back_populates="responsable")

    es = association_proxy('responsable_estancia', 'estancia')


class AuthResponsableToken(Base):
    __tablename__ = "auth_responsable_token"
    id_token = Column(Integer, primary_key=True)
    token = Column(String,unique=True,nullable=False)
    status = Column(Integer,server_default=FetchedValue())
    jti = Column(String,server_default=FetchedValue())
    created_at = Column(Integer,server_default=FetchedValue())
    id_responsable = Column(Integer,ForeignKey("responsable.id_responsable"))

    responsable = relationship("Responsable",back_populates="tokens",uselist=False)

class DispositivoResposable(Base):
    __tablename__ = "dispositivo_responsable"
    id_dispositivo_responsable = Column(Integer,primary_key=True)
    identifier =  Column(String,unique=True)
    id_responsable = Column(Integer,ForeignKey("responsable.id_responsable"))
    token_equipo = Column(String,nullable=False,default="")
    tipo_equipo = Column(Integer,nullable=False)
    responsable = relationship("Responsable",back_populates="dispositivos",cascade="all, delete")


class ResponsableEstancia(Base):
    __tablename__ = "responsable_estancia"
    id_responsable_estancia = Column(Integer,primary_key=True)
    id_responsable = Column(Integer,ForeignKey("responsable.id_responsable"),nullable=False)
    id_estancia = Column(Integer,ForeignKey("estancia.id_estancia"),nullable=False)

    responsable = relationship("Responsable",back_populates="responsable_estancia")
    estancia = relationship("Estancia",back_populates="responsable_estancia")
    

class ProcedimientoAutorizacion(Base):
    __tablename__ = "procedimiento_autorizacion"
    id_procedimiento_autorizacion = Column(Integer,primary_key=True)
    id_estancia = Column(Integer,ForeignKey("estancia.id_estancia"))
    id_responsable = Column(Integer,ForeignKey("responsable.id_responsable"))
    id_procedimiento_informe = Column(Integer,ForeignKey("procedimiento_informe.id_procedimiento_informe"))
    fecha_autorizacion = Column(types.DateTime)

    estancia = relationship("Estancia",back_populates="procedimiento_autorizacion")
    responsable = relationship("Responsable",back_populates="procedimiento_autorizacion")
    procedimiento_informe = relationship("ProcedimientoInforme",back_populates="procedimiento_autorizacion")


class ResponsableMedico(Base):
    __tablename__ = "responsable_medico"
    id_responsable_medico = Column(Integer,primary_key=True)
    identificador = Column(String,unique=True)
    nombre = Column(String,nullable=False)
    apellido_1 = Column(String,nullable=False)
    apellido_2 = Column(String,nullable=True)
    #email = Column(String,unique=True)
    id_hospital = Column(Integer,ForeignKey("hospital.id_hospital"))

    informes = relationship("Informe", back_populates="responsable_medico")


class Procedimiento(Base):
    __tablename__ = "procedimiento"
    id_procedimiento = Column(Integer,primary_key=True)
    nombre = Column(String,nullable=False)
    duracion_aproximada = Column(types.Numeric,nullable=False)
    costo = Column(types.Numeric,nullable=False)

    hospital_procedimiento = relationship("HospitalProcedimiento",back_populates="procedimiento")
    procedimiento_informe = relationship("ProcedimientoInforme",back_populates="procedimiento")

class HospitalProcedimiento(Base):
    __tablename__ = "hospital_procedimiento"
    id_hospital_procedimiento = Column(Integer,primary_key=True)
    id_hospital = Column(Integer,ForeignKey("hospital.id_hospital"))
    id_procedimiento = Column(Integer,ForeignKey("procedimiento.id_procedimiento"))

    procedimiento = relationship("Procedimiento",back_populates="hospital_procedimiento")
    hospital = relationship("Hospital",back_populates="hospital_procedimiento")
    



class Informe(Base):
    __tablename__ = "informe"
    id_informe = Column(Integer,primary_key=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    fecha = Column(types.DateTime,server_default=FetchedValue())
    id_estancia = Column(Integer,ForeignKey("estancia.id_estancia"))
    id_responsable_medico = Column(Integer, ForeignKey("responsable_medico.id_responsable_medico"))


    estancia = relationship("Estancia",back_populates="informes")
    notificaciones = relationship("Notificacion", back_populates="informe")
    responsable_medico = relationship("ResponsableMedico", back_populates="informes")
    procedimiento_informe = relationship("ProcedimientoInforme",back_populates="informe")


    @property
    def formatted_date(self):
        return self.fecha.strftime("%d/%m/%Y %H:%M:%S")


    def __repr__(self) -> str:
        return f"Id: {self.id_informe} titulo {self.titulo} descripcion {self.descripcion}"



class ProcedimientoInforme(Base):
    __tablename__ = "procedimiento_informe"
    id_procedimiento_informe = Column(Integer, primary_key=True)
    id_informe = Column(Integer,ForeignKey("informe.id_informe"))
    id_procedimiento = Column(Integer,ForeignKey("procedimiento.id_procedimiento"))

    informe = relationship("Informe",back_populates="procedimiento_informe")
    procedimiento = relationship("Procedimiento",back_populates="procedimiento_informe")
    procedimiento_autorizacion = relationship("ProcedimientoAutorizacion",back_populates="procedimiento_informe")

class Notificacion(Base):
    __tablename__ = "notificacion"
    id_notificacion = Column(Integer,primary_key=True)
    id_informe = Column(Integer,ForeignKey("informe.id_informe"))
    id_responsable = Column(Integer,ForeignKey("responsable.id_responsable"))
    active = Column(Integer,nullable=False,default=1)

    informe = relationship("Informe", back_populates="notificaciones",uselist=False)
    responsable = relationship("Responsable",back_populates="notificaciones")