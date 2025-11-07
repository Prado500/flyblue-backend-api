from sqlalchemy import Column, Integer, String, Boolean, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # Importa tu Base declarativa (de database.py)

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    contraseña = Column(String, nullable=False)
    rol = Column(String, nullable=False)  # 'usuario' o 'admin'

    reservas = relationship("Reserva", back_populates="usuario")


class Ciudad(Base):
    __tablename__ = "ciudades"

    id_ciudad = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    codigo = Column(String, nullable=False)

    vuelos_origen = relationship("Vuelo", back_populates="origen", foreign_keys="Vuelo.id_origen")
    vuelos_destino = relationship("Vuelo", back_populates="destino", foreign_keys="Vuelo.id_destino")


class Vuelo(Base):
    __tablename__ = "vuelos"

    id_vuelo = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, nullable=False)
    id_origen = Column(Integer, ForeignKey("ciudades.id_ciudad"))
    id_destino = Column(Integer, ForeignKey("ciudades.id_ciudad"))
    fecha_salida = Column(DateTime, nullable=False)
    fecha_llegada = Column(DateTime, nullable=False)
    precio_base = Column(DECIMAL(10, 2), nullable=False)
    asientos_totales = Column(Integer, nullable=False)
    asientos_disponibles = Column(Integer, nullable=False)

    origen = relationship("Ciudad", foreign_keys=[id_origen], back_populates="vuelos_origen")
    destino = relationship("Ciudad", foreign_keys=[id_destino], back_populates="vuelos_destino")
    asientos = relationship("Asiento", back_populates="vuelo")
    reservas = relationship("Reserva", back_populates="vuelo")


class Asiento(Base):
    __tablename__ = "asientos"

    id_asiento = Column(Integer, primary_key=True, index=True)
    id_vuelo = Column(Integer, ForeignKey("vuelos.id_vuelo"))
    fila = Column(Integer, nullable=False)
    columna = Column(String, nullable=False)
    disponible = Column(Boolean, default=True)

    vuelo = relationship("Vuelo", back_populates="asientos")
    reserva = relationship("Reserva", back_populates="asiento", uselist=False)


class Equipaje(Base):
    __tablename__ = "equipajes"

    id_equipaje = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)  # Pequeño, Mediano, Grande
    precio = Column(DECIMAL(10, 2), nullable=False)

    reservas = relationship("Reserva", back_populates="equipaje")


class Reserva(Base):
    __tablename__ = "reservas"

    id_reserva = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_vuelo = Column(Integer, ForeignKey("vuelos.id_vuelo"))
    id_asiento = Column(Integer, ForeignKey("asientos.id_asiento"))
    id_equipaje = Column(Integer, ForeignKey("equipajes.id_equipaje"))
    total = Column(DECIMAL(10, 2), nullable=False)

    usuario = relationship("Usuario", back_populates="reservas")
    vuelo = relationship("Vuelo", back_populates="reservas")
    asiento = relationship("Asiento", back_populates="reserva")
    equipaje = relationship("Equipaje", back_populates="reservas")
    pago = relationship("Pago", back_populates="reserva", uselist=False)


class Pago(Base):
    __tablename__ = "pagos"

    id_pago = Column(Integer, primary_key=True, index=True)
    id_reserva = Column(Integer, ForeignKey("reservas.id_reserva"))
    monto = Column(DECIMAL(10, 2), nullable=False)
    estado = Column(String, nullable=False)  # pagado, fallido
    fecha = Column(DateTime, nullable=False)

    reserva = relationship("Reserva", back_populates="pago")
