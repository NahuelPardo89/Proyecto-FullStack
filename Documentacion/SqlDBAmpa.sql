-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema u781791491_AMPA
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema u781791491_AMPA
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `u781791491_AMPA` DEFAULT CHARACTER SET utf8 ;
USE `u781791491_AMPA` ;

-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`instalaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`instalaciones` (
  `idInstalacion` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`idInstalacion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`departamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`departamento` (
  `idDepto` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idDepto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`departamentoCiudad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`departamentoCiudad` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`ciudad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`ciudad` (
  `idciudad` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `codigopostal` VARCHAR(45) NOT NULL,
  `departamentoCiudad_id` INT NOT NULL,
  PRIMARY KEY (`idciudad`),
  INDEX `fk_ciudad_departamentoCiudad1_idx` (`departamentoCiudad_id` ASC) VISIBLE,
  CONSTRAINT `fk_ciudad_departamentoCiudad1`
    FOREIGN KEY (`departamentoCiudad_id`)
    REFERENCES `u781791491_AMPA`.`departamentoCiudad` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`users` (
  `dni` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `Telefono` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  `contraseña` VARCHAR(45) NOT NULL,
  `ciudad_idciudad` INT NOT NULL,
  PRIMARY KEY (`dni`),
  INDEX `fk_users_ciudad1_idx` (`ciudad_idciudad` ASC) VISIBLE,
  CONSTRAINT `fk_users_ciudad1`
    FOREIGN KEY (`ciudad_idciudad`)
    REFERENCES `u781791491_AMPA`.`ciudad` (`idciudad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`empleados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`empleados` (
  `idEmpleado` INT NOT NULL AUTO_INCREMENT,
  `idDepartamento` INT NOT NULL,
  `idInstalacion` INT NOT NULL,
  `Horario` VARCHAR(45) NOT NULL,
  `users_idPersona` INT NOT NULL,
  PRIMARY KEY (`idEmpleado`, `users_idPersona`),
  INDEX `IdDepartamento_idx` (`idDepartamento` ASC) VISIBLE,
  INDEX `idInstalacion_idx` (`idInstalacion` ASC) VISIBLE,
  INDEX `fk_empleados_users1_idx` (`users_idPersona` ASC) VISIBLE,
  CONSTRAINT `IdDepartamentoPersonal`
    FOREIGN KEY (`idDepartamento`)
    REFERENCES `u781791491_AMPA`.`departamento` (`idDepto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idInstalacionPersonal`
    FOREIGN KEY (`idInstalacion`)
    REFERENCES `u781791491_AMPA`.`instalaciones` (`idInstalacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_empleados_users1`
    FOREIGN KEY (`users_idPersona`)
    REFERENCES `u781791491_AMPA`.`users` (`dni`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`Proveedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`Proveedores` (
  `idProveedor` INT NOT NULL AUTO_INCREMENT,
  `idEmpleado` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `empresa` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idProveedor`),
  INDEX `idEmpleadoProveedor_idx` (`idEmpleado` ASC) VISIBLE,
  CONSTRAINT `idEmpleadoProveedor`
    FOREIGN KEY (`idEmpleado`)
    REFERENCES `u781791491_AMPA`.`empleados` (`idEmpleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`categoria` (
  `idcategoria` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`idcategoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`productos` (
  `idProd` INT NOT NULL AUTO_INCREMENT,
  `idProveedor` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `marca` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  `precio` INT NOT NULL,
  `stock` INT NOT NULL,
  `foto` VARCHAR(5000) NOT NULL,
  `categoria_idcategoria` INT NOT NULL,
  PRIMARY KEY (`idProd`),
  INDEX `Idproveedor_idx` (`idProveedor` ASC) VISIBLE,
  INDEX `fk_productos_categoria1_idx` (`categoria_idcategoria` ASC) VISIBLE,
  CONSTRAINT `IdproveedorProd`
    FOREIGN KEY (`idProveedor`)
    REFERENCES `u781791491_AMPA`.`Proveedores` (`idProveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_productos_categoria1`
    FOREIGN KEY (`categoria_idcategoria`)
    REFERENCES `u781791491_AMPA`.`categoria` (`idcategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`Clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`Clientes` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `socio` TINYINT NOT NULL,
  `users_idPersona` INT NOT NULL,
  PRIMARY KEY (`idCliente`, `users_idPersona`),
  INDEX `fk_Clientes_users1_idx` (`users_idPersona` ASC) VISIBLE,
  CONSTRAINT `fk_Clientes_users1`
    FOREIGN KEY (`users_idPersona`)
    REFERENCES `u781791491_AMPA`.`users` (`dni`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`CarritoProductos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`CarritoProductos` (
  `idCarrito` INT NOT NULL AUTO_INCREMENT,
  `idCliente` INT NOT NULL,
  `idPersonal` INT NOT NULL,
  PRIMARY KEY (`idCarrito`),
  INDEX `idClientes_idx` (`idCliente` ASC) VISIBLE,
  INDEX `idPersonal_idx` (`idPersonal` ASC) VISIBLE,
  CONSTRAINT `idClientesCarritoP`
    FOREIGN KEY (`idCliente`)
    REFERENCES `u781791491_AMPA`.`Clientes` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idPersonalCarritoP`
    FOREIGN KEY (`idPersonal`)
    REFERENCES `u781791491_AMPA`.`empleados` (`idEmpleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`detalleCarritoProductos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`detalleCarritoProductos` (
  `idDetalle` INT NOT NULL AUTO_INCREMENT,
  `idCarrito` INT NOT NULL,
  `idProducto` INT NOT NULL,
  `cantidad` INT NOT NULL,
  `monto` INT NOT NULL,
  PRIMARY KEY (`idDetalle`),
  INDEX `idCarrito_idx` (`idCarrito` ASC) VISIBLE,
  INDEX `idProd_idx` (`idProducto` ASC) VISIBLE,
  CONSTRAINT `idCarritoDetalle`
    FOREIGN KEY (`idCarrito`)
    REFERENCES `u781791491_AMPA`.`CarritoProductos` (`idCarrito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idProdDetalle`
    FOREIGN KEY (`idProducto`)
    REFERENCES `u781791491_AMPA`.`productos` (`idProd`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`CarritoReservas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`CarritoReservas` (
  `idCarrito` INT NOT NULL AUTO_INCREMENT,
  `idCliente` INT NOT NULL,
  `idPersonal` INT NOT NULL,
  PRIMARY KEY (`idCarrito`),
  INDEX `idClientes_idx` (`idCliente` ASC) VISIBLE,
  INDEX `idePersonal_idx` (`idPersonal` ASC) VISIBLE,
  CONSTRAINT `idClienteCarritoR`
    FOREIGN KEY (`idCliente`)
    REFERENCES `u781791491_AMPA`.`Clientes` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idPerdonalCarritoR`
    FOREIGN KEY (`idPersonal`)
    REFERENCES `u781791491_AMPA`.`empleados` (`idEmpleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`detalleCarritoReservas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`detalleCarritoReservas` (
  `idDetalle` INT NOT NULL AUTO_INCREMENT,
  `fechaHora` VARCHAR(45) NULL,
  `idInstalacion` INT NOT NULL,
  `idCarritoReservas` INT NOT NULL,
  `cantidad` INT NOT NULL,
  `monto` INT NOT NULL,
  PRIMARY KEY (`idDetalle`),
  INDEX `idInstalacion_idx` (`idInstalacion` ASC) VISIBLE,
  INDEX `idCarritoReserva_idx` (`idCarritoReservas` ASC) VISIBLE,
  CONSTRAINT `idInstalacionDetalle`
    FOREIGN KEY (`idInstalacion`)
    REFERENCES `u781791491_AMPA`.`instalaciones` (`idInstalacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idCarritoReservaDetalle`
    FOREIGN KEY (`idCarritoReservas`)
    REFERENCES `u781791491_AMPA`.`CarritoReservas` (`idCarrito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `u781791491_AMPA`.`Factura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u781791491_AMPA`.`Factura` (
  `idFactura` INT NOT NULL,
  `fecha` DATE NOT NULL,
  `subTotal` INT NOT NULL,
  `descuento` INT NULL,
  `total` INT NOT NULL,
  `Clientes_idCliente` INT NOT NULL,
  `CarritoProductos_idCarrito` INT NOT NULL,
  `CarritoReservas_idCarrito` INT NOT NULL,
  INDEX `fk_Factura_Clientes1_idx` (`Clientes_idCliente` ASC) VISIBLE,
  INDEX `fk_Factura_CarritoProductos1_idx` (`CarritoProductos_idCarrito` ASC) VISIBLE,
  INDEX `fk_Factura_CarritoReservas1_idx` (`CarritoReservas_idCarrito` ASC) VISIBLE,
  CONSTRAINT `fk_Factura_Clientes1`
    FOREIGN KEY (`Clientes_idCliente`)
    REFERENCES `u781791491_AMPA`.`Clientes` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Factura_CarritoProductos1`
    FOREIGN KEY (`CarritoProductos_idCarrito`)
    REFERENCES `u781791491_AMPA`.`CarritoProductos` (`idCarrito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Factura_CarritoReservas1`
    FOREIGN KEY (`CarritoReservas_idCarrito`)
    REFERENCES `u781791491_AMPA`.`CarritoReservas` (`idCarrito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
