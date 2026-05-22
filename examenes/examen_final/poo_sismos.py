"""
Ejercicio 5 — Programación Orientada a Objetos
Examen Final — Programación 1 (F12) — Variante A: Sismos USGS
"""

class EventoSismico:
    """Representa un evento sísmico genérico."""

    def __init__(self, lugar, fecha):
        self.lugar = lugar
        self.fecha = fecha

    def clasificar(self):
        pass

    def descripcion(self):
        pass

    def __str__(self):
        return self.descripcion() or f"EventoSismico en {self.lugar}"

    def __repr__(self):
        return f"{self.__class__.__name__}(lugar={self.lugar!r}, fecha={self.fecha!r})"


class Sismo(EventoSismico):
    """Representa un sismo con sus atributos medidos."""

    def __init__(self, lugar, fecha, magnitud, profundidad, tipo_escala="mww"):
        super().__init__(lugar, fecha)
        self.magnitud = magnitud
        self.profundidad = profundidad
        self.tipo_escala = tipo_escala

    def clasificar(self):
        """Clasifica el sismo según su magnitud."""
        if self.magnitud >= 8.0:
            return 'Gran terremoto'
        elif self.magnitud >= 7.0:
            return 'Mayor'
        elif self.magnitud >= 6.0:
            return 'Fuerte'
        elif self.magnitud >= 5.5:
            return 'Moderado-Fuerte'
        else:
            return 'No clasificado'

    def clasificar_profundidad(self):
        """Clasifica el sismo según la profundidad del foco."""
        if self.profundidad < 70:
            return 'Superficial'
        elif self.profundidad < 300:
            return 'Intermedio'
        else:
            return 'Profundo'

    def es_peligroso(self):
        """Retorna True si magnitud >= 7.0 Y profundidad < 70 km."""
        return self.magnitud >= 7.0 and self.profundidad < 70

    def descripcion(self):
        """Retorna una descripción formateada del sismo."""
        return (
            f"Sismo mag={self.magnitud:.2f} | {self.clasificar()} | "
            f"{self.clasificar_profundidad()} | Lugar: {self.lugar} | "
            f"Escala: {self.tipo_escala}"
        )

    def __str__(self):
        return self.descripcion()

    def __repr__(self):
        return (
            f"Sismo(lugar={self.lugar!r}, magnitud={self.magnitud}, "
            f"profundidad={self.profundidad}, tipo_escala={self.tipo_escala!r})"
        )


class CatalogoSismos:
    """Colección de objetos Sismo con métodos de consulta y resumen."""

    def __init__(self, nombre="Catálogo de Sismos"):
        self.nombre = nombre
        self._sismos = []

    def agregar(self, sismo):
        """Agrega un objeto Sismo al catálogo."""
        self._sismos.append(sismo)

    def __len__(self):
        """Retorna el total de sismos en el catálogo."""
        return len(self._sismos)

    def el_mas_intenso(self):
        """Encuentra el sismo con la mayor magnitud."""
        if not self._sismos:
            return None
        sismo_max = self._sismos[0]
        for sismo in self._sismos[1:]:
            if sismo.magnitud > sismo_max.magnitud:
                sismo_max = sismo
        return sismo_max

    def filtrar_por_categoria(self, categoria):
        """Retorna una lista con todos los sismos de la categoría dada."""
        resultado = []
        for sismo in self._sismos:
            if sismo.clasificar() == categoria:
                resultado.append(sismo)
        return resultado

    def resumen(self):
        """Imprime un resumen del catálogo."""
        print(f"Catálogo: {self.nombre}")
        print(f"Total de sismos: {len(self)}\n")
        mas_intenso = self.el_mas_intenso()
        if mas_intenso:
            print(f"Sismo más intenso:")
            print(f"  {mas_intenso}\n")
        print("Distribución por categoría:")
        categorias = ['Moderado-Fuerte', 'Fuerte', 'Mayor', 'Gran terremoto']
        for cat in categorias:
            sismos_cat = self.filtrar_por_categoria(cat)
            print(f"  {cat:20s} : {len(sismos_cat):3d} sismos")

