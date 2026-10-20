_user = None
_participant = None
_event = None

def user_data_by_username():
    global _user

    if _user is None:
        _user = {
            "Kiya": {
                "id": 1,
                "password": "123",
                "role": "Admin",
                "email": "antoniuskiya57@gmail.com",
                "gender": "Laki-laki",
                "phone": "081234567890",
                "address": "Yogyakarta",
            },
            "Kevin": {
                "id": 2,
                "password": "321",
                "role": "Peserta",
                "email": "kevin@example.com",
                "gender": "Laki-laki",
                "phone": "081234567891",
                "address": "Sleman",
            },
            "Semmi": {
                "id": 3,
                "password": "staff",
                "role": "Staff",
                "email": "semmi@example.com",
                "gender": "Perempuan",
                "phone": None,
                "address": None,
            },
            "Calis": {
                "id": 4,
                "password": "calis123",
                "role": "Pengunjung",
                "email": None,
                "gender": None,
                "phone": None,
                "address": None,
            },
            "Yumeko": {
                "id": 5,
                "password": "calis123",
                "role": "Pengunjung",
                "email": None,
                "gender": None,
                "phone": None,
                "address": None,
            },
            "Radit": {
                "id": 6,
                "password": "nugroho123",
                "role": "Pengunjung",
                "email": "nugroho@tampan.com",
                "gender": "Laki-laki",
                "phone": None,
                "address": "Yogyakarta",
            },
            "Pak Willy": {
                "id": 7,
                "password": "123",
                "role": "Peserta",
                "email": "willysr@gmail.com",
                "gender": "Laki-laki",
                "phone": "081234567890",
                "address": "Yogyakarta",
            },
        }

    return _user

def participant_data_by_id():
    global _participant
    if _participant is None:
        _participant = {
            "ID01": {
                "user_id" : 2,
                "status_bayar": "Paid",
                "status_tiket": "Belum Check-In"
            },
            "ID501": {
                "user_id" : 7,
                "status_bayar": "Invitation",
                "status_tiket": "Belum Check-In"
            }
        }
    return _participant

def event_data():
    global _event
    # satu dictionary besar buat semua info event
    if _event is None:
        _event = {
            "info": {
                "nama": "Japfest UKDW 2026",
                "tanggal": "2026-12-06",
                "lokasi": "Auditorium Koinonia, UKDW, Yogyakarta",
                "deskripsi": "Festival musik dan teknologi tahunan.",
                "harga_tiket": 15000,
                "kuota": 4,
            },
            "sponsor": [
                {"nama": "Bethesda", "tier": "Gold"},
                {"nama": "SiMayGramin", "tier": "Gold"},
                {"nama": "FTI", "tier": "Silver"},
            ],
            "pengisi_acara": [
                {"nama": "Kohi Sekai", "jenis": "Idol performance"},
                {"nama": "Minerva Land", "jenis": "Dance"},
            ],
            "rundown": [
                {"jam": "09:00", "acara": "Registrasi & Check-in"},
                {"jam": "10:00", "acara": "Pembukaan"},
                {"jam": "13:00", "acara": "Talkshow"},
            ],
        }

    return _event
