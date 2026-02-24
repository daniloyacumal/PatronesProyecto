# Sistema de Gestión de Órdenes Médicas y Notificaciones Clínicas
Proyecto de aplicación para Patrones de Desarrollo Web

│
├── app.py
├── config/
│   └── database.py
├── factory/
│   └── order_factory.py
├── models/
│   ├── order.py
│   ├── lab_order.py
│   ├── medication_order.py
│   └── procedure_order.py
├── strategies/
│   ├── payment_strategy.py
│   ├── eps_strategy.py
│   ├── private_strategy.py
│   └── insurance_strategy.py
├── observers/
│   ├── observer.py
│   ├── patient_notifier.py
│   ├── pharmacy_notifier.py
│   └── doctor_notifier.py
