CREATE TABLE Habitacion (
	hab_codigo INT PRIMARY KEY,
	hab_numero INT NOT NULL
);

CREATE TABLE Pension (
	pen_codigo INT PRIMARY KEY,
	pen_nombre VARCHAR(50) NOT NULL,
	pen_precio DECIMAL(2,2) NOT NULL
);

CREATE TABLE Marca (
	mar_codigo INT PRIMARY KEY,
	mar_nombre  VARCHAR(50)
);

CREATE TABLE Vehiculo (
	veh_codigo INT PRIMARY KEY,
	veh_patente VARCHAR(15) NOT NULL,
	veh_IDmarca INT NOT NULL
);

ALTER TABLE Vehiculo
ADD CONSTRAINT fk_vehiculo_marca
FOREIGN KEY (veh_IDmarca)
REFERENCES Marca(mar_codigo);

CREATE TABLE VehiculoCliente (
	vc_codigo INT PRIMARY KEY,
	vc_vehiculo INT NOT NULL
);

ALTER TABLE VehiculoCliente
ADD CONSTRAINT fk_vehiculocliente_vehiculo
FOREIGN KEY (vc_vehiculo)
REFERENCES Vehiculo(veh_codigo);

CREATE TABLE Cliente (
	cli_codigo INT PRIMARY KEY,
	cli_nombre VARCHAR(50) NOT NULL,
	cli_apellido VARCHAR(50) NOT NULL,
	cli_nroDocumento VARCHAR(8) NOT NULL,
	cli_IDvehcliente INT NOT NULL
);

ALTER TABLE Cliente
ADD CONSTRAINT fk_Cliente_VehiculoCliente
FOREIGN KEY (cli_IDvehcliente) REFERENCES VehiculoCliente(vc_codigo)

CREATE TABLE Estadia (
	est_codigo INT PRIMARY KEY,
	est_fechaInicio DATETIME NOT NULL,
	est_fechaFin DATETIME NOT NULL,
	est_acompanante SMALLINT NOT NULL,
	est_totalEstadia DECIMAL(10,2) NOT NULL,
	est_IDpension INT NOT NULL,
	est_IDhabitacion INT NOT NULL,
	est_IDcliente INT NOT NULL
);

ALTER TABLE Estadia
ADD CONSTRAINT fk_Estadia_Cliente
FOREIGN KEY (est_IDcliente) 
REFERENCES Cliente(cli_codigo)

ALTER TABLE Estadia
ADD CONSTRAINT fk_Estadia_Habitacion
FOREIGN KEY (est_IDhabitacion) 
REFERENCES Habitacion(hab_codigo)

ALTER TABLE Estadia
ADD CONSTRAINT fk_Estadia_Pension
FOREIGN KEY (est_IDpension) 
REFERENCES Pension(pen_codigo)