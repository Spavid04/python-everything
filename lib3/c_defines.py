# This is a generated file, created by generate_headers.py
# Changes made here will be lost when re-running that script
# Input Everything3.h SHA256: 5ccadde782b3a4ddd6429a0439d6b3da1ba722fa148d7d04ecc07831cd4706dd

import enum
import typing


#region Status
class Status(enum.IntEnum):
    OK = 0
    OUT_OF_MEMORY = 0xE0000001
    IPC_PIPE_NOT_FOUND = 0xE0000002
    DISCONNECTED = 0xE0000003
    INVALID_PARAMETER = 0xE0000004
    BAD_REQUEST = 0xE0000005
    CANCELLED = 0xE0000006
    PROPERTY_NOT_FOUND = 0xE0000007
    SERVER = 0xE0000008
    INVALID_COMMAND = 0xE0000009
    BAD_RESPONSE = 0xE000000A
    INSUFFICIENT_BUFFER = 0xE000000B
    SHUTDOWN = 0xE000000C
    INVALID_PROPERTY_VALUE_TYPE = 0xE000000D

StatusToMessageMap = {
    Status.OK: "no error",
    Status.OUT_OF_MEMORY: "out of memory.",
    Status.IPC_PIPE_NOT_FOUND: "IPC pipe server not found (Everything search client is not running)",
    Status.DISCONNECTED: "disconnected from pipe server",
    Status.INVALID_PARAMETER: "invalid parameter",
    Status.BAD_REQUEST: "bad request",
    Status.CANCELLED: "user cancelled",
    Status.PROPERTY_NOT_FOUND: "property not found",
    Status.SERVER: "server error (server out of memory)",
    Status.INVALID_COMMAND: "invalid command",
    Status.BAD_RESPONSE: "bad server response",
    Status.INSUFFICIENT_BUFFER: "not enough room to store response data",
    Status.SHUTDOWN: "shutdown initiated by user",
    Status.INVALID_PROPERTY_VALUE_TYPE: "property value type is incorrect.",
}

def StatusToMessage(status: Status) -> str:
    return StatusToMessageMap.get(status, "<unknown error>")

#region Exceptions
class Everything3Exception(Exception):
    def __init__(self, *args, status: Status):
        super().__init__(*args)
        self.status = status

class E3OutOfMemoryError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.OUT_OF_MEMORY)
class E3IpcPipeNotFoundError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.IPC_PIPE_NOT_FOUND)
class E3DisconnectedError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.DISCONNECTED)
class E3InvalidParameterError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.INVALID_PARAMETER)
class E3BadRequestError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.BAD_REQUEST)
class E3CancelledError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.CANCELLED)
class E3PropertyNotFoundError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.PROPERTY_NOT_FOUND)
class E3ServerError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.SERVER)
class E3InvalidCommandError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.INVALID_COMMAND)
class E3BadResponseError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.BAD_RESPONSE)
class E3InsufficientBufferError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.INSUFFICIENT_BUFFER)
class E3ShutdownError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.SHUTDOWN)
class E3InvalidPropertyValueTypeError(Everything3Exception):
    def __init__(self, *args):
        super().__init__(*args, status=Status.INVALID_PROPERTY_VALUE_TYPE)

StatusToExceptionTypeMap = {
    Status.OUT_OF_MEMORY: E3OutOfMemoryError,
    Status.IPC_PIPE_NOT_FOUND: E3IpcPipeNotFoundError,
    Status.DISCONNECTED: E3DisconnectedError,
    Status.INVALID_PARAMETER: E3InvalidParameterError,
    Status.BAD_REQUEST: E3BadRequestError,
    Status.CANCELLED: E3CancelledError,
    Status.PROPERTY_NOT_FOUND: E3PropertyNotFoundError,
    Status.SERVER: E3ServerError,
    Status.INVALID_COMMAND: E3InvalidCommandError,
    Status.BAD_RESPONSE: E3BadResponseError,
    Status.INSUFFICIENT_BUFFER: E3InsufficientBufferError,
    Status.SHUTDOWN: E3ShutdownError,
    Status.INVALID_PROPERTY_VALUE_TYPE: E3InvalidPropertyValueTypeError,
}

def StatusToExceptionType(status: Status) -> typing.Optional[typing.Type[Everything3Exception]]:
    return StatusToExceptionTypeMap.get(status, None)
#endregion
#endregion

#region Target Machine
class TargetMachine(enum.IntEnum):
    UNKNOWN = 0
    X86 = 1
    X64 = 2
    ARM = 3
    ARM64 = 4
#endregion

#region Folder First Option
class FolderFirst(enum.IntEnum):
    ASCENDING = 0
    ALWAYS = 1
    NEVER = 2
    DESCENDING = 3
#endregion

#region Property Type
class PropertyType(enum.IntEnum):
    NONE = 0
    METADATA = 1
    FILE = 2
    INDEX = 3
    CONTENT = 4
    VOLUME = 5
    SEARCH = 6
    PROPERTY_SYSTEM = 7
#endregion

#region Property Value
class PropertyType(enum.IntEnum):
    NULL = 0
    BYTE = 1
    WORD = 2
    DWORD = 3
    DWORD_FIXED_Q1K = 4
    UINT64 = 5
    UINT128 = 6
    DIMENSIONS = 7
    PSTRING = 8
    PSTRING_MULTISTRING = 9
    PSTRING_STRING_REFERENCE = 10
    SIZE_T = 11
    INT32_FIXED_Q1K = 12
    INT32_FIXED_Q1M = 13
    PSTRING_FOLDER_REFERENCE = 14
    PSTRING_FILE_OR_FOLDER_REFERENCE = 15
    BLOB8 = 16
    DWORD_GET_TEXT = 17
    WORD_GET_TEXT = 18
    BLOB16 = 19
    BYTE_GET_TEXT = 20
    PROPVARIANT = 21
#endregion

#region Property ID
class PropertyId(enum.IntEnum):
    INVALID_PROPERTY_ID = -1
    NAME = 0
    PATH = 1
    SIZE = 2
    EXTENSION = 3
    TYPE = 4
    DATE_MODIFIED = 5
    DATE_CREATED = 6
    DATE_ACCESSED = 7
    ATTRIBUTES = 8
    DATE_RECENTLY_CHANGED = 9
    RUN_COUNT = 10
    DATE_RUN = 11
    FILE_LIST_FILENAME = 12
    WIDTH = 13
    HEIGHT = 14
    DIMENSIONS = 15
    ASPECT_RATIO = 16
    BIT_DEPTH = 17
    LENGTH = 18
    AUDIO_SAMPLE_RATE = 19
    AUDIO_CHANNELS = 20
    AUDIO_BITS_PER_SAMPLE = 21
    AUDIO_BIT_RATE = 22
    AUDIO_FORMAT = 23
    FILE_SIGNATURE = 24
    TITLE = 25
    ARTIST = 26
    ALBUM = 27
    YEAR = 28
    COMMENT = 29
    TRACK = 30
    GENRE = 31
    FRAME_RATE = 32
    VIDEO_BIT_RATE = 33
    VIDEO_FORMAT = 34
    RATING = 35
    TAGS = 36
    MD5 = 37
    SHA1 = 38
    SHA256 = 39
    CRC32 = 40
    SIZE_ON_DISK = 41
    DESCRIPTION = 42
    VERSION = 43
    PRODUCT_NAME = 44
    PRODUCT_VERSION = 45
    COMPANY = 46
    KIND = 47
    FILE_NAME_LENGTH = 48
    FULL_PATH_LENGTH = 49
    SUBJECT = 50
    AUTHORS = 51
    DATE_TAKEN = 52
    SOFTWARE = 53
    DATE_ACQUIRED = 54
    COPYRIGHT = 55
    IMAGE_ID = 56
    HORIZONTAL_RESOLUTION = 57
    VERTICAL_RESOLUTION = 58
    COMPRESSION = 59
    RESOLUTION_UNIT = 60
    COLOR_REPRESENTATION = 61
    COMPRESSED_BITS_PER_PIXEL = 62
    CAMERA_MAKER = 63
    CAMERA_MODEL = 64
    F_STOP = 65
    EXPOSURE_TIME = 66
    ISO_SPEED = 67
    EXPOSURE_BIAS = 68
    FOCAL_LENGTH = 69
    MAX_APERTURE = 70
    METERING_MODE = 71
    SUBJECT_DISTANCE = 72
    FLASH_MODE = 73
    FLASH_ENERGY = 74
    LENS_MAKER = 76
    LENS_MODEL = 77
    FLASH_MAKER = 78
    FLASH_MODEL = 79
    CAMERA_SERIAL_NUMBER = 80
    CONTRAST = 81
    BRIGHTNESS = 82
    LIGHT_SOURCE = 83
    EXPOSURE_PROGRAM = 84
    SATURATION = 85
    SHARPNESS = 86
    WHITE_BALANCE = 87
    PHOTOMETRIC_INTERPRETATION = 88
    DIGITAL_ZOOM = 89
    EXIF_VERSION = 90
    LATITUDE = 91
    LONGITUDE = 92
    ALTITUDE = 93
    SUBTITLE = 94
    TOTAL_BIT_RATE = 95
    DIRECTORS = 96
    PRODUCERS = 97
    WRITERS = 98
    PUBLISHER = 99
    CONTENT_DISTRIBUTOR = 100
    DATE_ENCODED = 101
    ENCODED_BY = 102
    AUTHOR_URL = 103
    PROMOTION_URL = 104
    OFFLINE_AVAILABILITY = 105
    OFFLINE_STATUS = 106
    SHARED_WITH = 107
    OWNER = 108
    COMPUTER = 109
    ALBUM_ARTIST = 110
    PARENTAL_RATING_REASON = 111
    COMPOSER = 112
    CONDUCTOR = 113
    CONTENT_GROUP_DESCRIPTION = 114
    MOOD = 115
    PART_OF_SET = 116
    INITIAL_KEY = 117
    BEATS_PER_MINUTE = 118
    PROTECTED = 119
    PART_OF_A_COMPILATION = 120
    PARENTAL_RATING = 121
    PERIOD = 122
    PEOPLE = 123
    CATEGORY = 124
    CONTENT_STATUS = 125
    DOCUMENT_CONTENT_TYPE = 126
    PAGE_COUNT = 127
    WORD_COUNT = 128
    CHARACTER_COUNT = 129
    LINE_COUNT = 130
    PARAGRAPH_COUNT = 131
    TEMPLATE = 132
    SCALE = 133
    LINKS_DIRTY = 134
    LANGUAGE = 135
    LAST_AUTHOR = 136
    REVISION_NUMBER = 137
    VERSION_NUMBER = 138
    MANAGER = 139
    DATE_CONTENT_CREATED = 140
    DATE_SAVED = 141
    DATE_PRINTED = 142
    TOTAL_EDITING_TIME = 143
    ORIGINAL_FILE_NAME = 144
    DATE_RELEASED = 145
    SLIDE_COUNT = 146
    NOTE_COUNT = 147
    HIDDEN_SLIDE_COUNT = 148
    PRESENTATION_FORMAT = 149
    TRADEMARKS = 150
    DISPLAY_NAME = 151
    FILE_NAME_LENGTH_IN_UTF8_BYTES = 152
    FULL_PATH_LENGTH_IN_UTF8_BYTES = 153
    CHILD_COUNT = 154
    CHILD_FOLDER_COUNT = 155
    CHILD_FILE_COUNT = 156
    CHILD_COUNT_FROM_DISK = 157
    CHILD_FOLDER_COUNT_FROM_DISK = 158
    CHILD_FILE_COUNT_FROM_DISK = 159
    FOLDER_DEPTH = 160
    TOTAL_SIZE = 161
    TOTAL_SIZE_ON_DISK = 162
    DATE_CHANGED = 163
    HARD_LINK_COUNT = 164
    DELETE_PENDING = 165
    IS_DIRECTORY = 166
    ALTERNATE_DATA_STREAM_COUNT = 167
    ALTERNATE_DATA_STREAM_NAMES = 168
    TOTAL_ALTERNATE_DATA_STREAM_SIZE = 169
    TOTAL_ALTERNATE_DATA_STREAM_SIZE_ON_DISK = 170
    COMPRESSED_SIZE = 171
    COMPRESSION_FORMAT = 172
    COMPRESSION_UNIT_SHIFT = 173
    COMPRESSION_CHUNK_SHIFT = 174
    COMPRESSION_CLUSTER_SHIFT = 175
    COMPRESSION_RATIO = 176
    REPARSE_TAG = 177
    REMOTE_PROTOCOL = 178
    REMOTE_PROTOCOL_VERSION = 179
    REMOTE_PROTOCOL_FLAGS = 180
    LOGICAL_BYTES_PER_SECTOR = 181
    PHYSICAL_BYTES_PER_SECTOR_FOR_ATOMICITY = 182
    PHYSICAL_BYTES_PER_SECTOR_FOR_PERFORMANCE = 183
    EFFECTIVE_PHYSICAL_BYTES_PER_SECTOR_FOR_ATOMICITY = 184
    FILE_STORAGE_INFO_FLAGS = 185
    BYTE_OFFSET_FOR_SECTOR_ALIGNMENT = 186
    BYTE_OFFSET_FOR_PARTITION_ALIGNMENT = 187
    ALIGNMENT_REQUIREMENT = 188
    VOLUME_SERIAL_NUMBER = 189
    FILE_ID = 190
    FRAME_COUNT = 191
    CLUSTER_SIZE = 192
    SECTOR_SIZE = 193
    AVAILABLE_FREE_DISK_SIZE = 194
    FREE_DISK_SIZE = 195
    TOTAL_DISK_SIZE = 196
    MAXIMUM_COMPONENT_LENGTH = 198
    FILE_SYSTEM_FLAGS = 199
    FILE_SYSTEM = 200
    ORIENTATION = 201
    END_OF_FILE = 202
    SHORT_NAME = 203
    SHORT_FULL_PATH = 204
    ENCRYPTION_STATUS = 205
    HARD_LINK_FILE_NAMES = 206
    INDEX_TYPE = 207
    DRIVE_TYPE = 208
    BINARY_TYPE = 209
    REGEX_MATCH_0 = 210
    REGEX_MATCH_1 = 211
    REGEX_MATCH_2 = 212
    REGEX_MATCH_3 = 213
    REGEX_MATCH_4 = 214
    REGEX_MATCH_5 = 215
    REGEX_MATCH_6 = 216
    REGEX_MATCH_7 = 217
    REGEX_MATCH_8 = 218
    REGEX_MATCH_9 = 219
    SIBLING_COUNT = 220
    SIBLING_FOLDER_COUNT = 221
    SIBLING_FILE_COUNT = 222
    INDEX_NUMBER = 223
    SHORTCUT_TARGET = 224
    OUT_OF_DATE = 225
    INCUR_SEEK_PENALTY = 226
    PLAIN_TEXT_LINE_COUNT = 227
    APERTURE = 228
    MAKER_NOTE = 229
    RELATED_SOUND_FILE = 230
    SHUTTER_SPEED = 231
    TRANSCODED_FOR_SYNC = 232
    CASE_SENSITIVE_DIR = 233
    DATE_INDEXED = 234
    NAME_FREQUENCY = 235
    SIZE_FREQUENCY = 236
    EXTENSION_FREQUENCY = 237
    REGEX_MATCHES = 238
    URL = 239
    FULL_PATH = 240
    PARENT_FILE_ID = 241
    SHA512 = 242
    SHA384 = 243
    CRC64 = 244
    FIRST_BYTE = 245
    FIRST_2_BYTES = 246
    FIRST_4_BYTES = 247
    FIRST_8_BYTES = 248
    FIRST_16_BYTES = 249
    FIRST_32_BYTES = 250
    FIRST_64_BYTES = 251
    FIRST_128_BYTES = 252
    LAST_BYTE = 253
    LAST_2_BYTES = 254
    LAST_4_BYTES = 255
    LAST_8_BYTES = 256
    LAST_16_BYTES = 257
    LAST_32_BYTES = 258
    LAST_64_BYTES = 259
    LAST_128_BYTES = 260
    BYTE_ORDER_MARK = 261
    VOLUME_LABEL = 262
    FILE_LIST_FULL_PATH = 263
    DISPLAY_FULL_PATH = 264
    PARSE_NAME = 265
    PARSE_FULL_PATH = 266
    STEM = 267
    SHELL_ATTRIBUTES = 268
    IS_FOLDER = 269
    VALID_UTF8 = 270
    STEM_LENGTH = 271
    EXTENSION_LENGTH = 272
    PATH_PART_LENGTH = 273
    TIME_MODIFIED = 274
    TIME_CREATED = 275
    TIME_ACCESSED = 276
    DAY_MODIFIED = 277
    DAY_CREATED = 278
    DAY_ACCESSED = 279
    PARENT_NAME = 280
    REPARSE_TARGET = 281
    DESCENDANT_COUNT = 282
    DESCENDANT_FOLDER_COUNT = 283
    DESCENDANT_FILE_COUNT = 284
    FROM = 285
    TO = 286
    DATE_RECEIVED = 287
    DATE_SENT = 288
    CONTAINER_FILENAMES = 289
    CONTAINER_FILE_COUNT = 290
    CUSTOM_PROPERTY_0 = 291
    CUSTOM_PROPERTY_1 = 292
    CUSTOM_PROPERTY_2 = 293
    CUSTOM_PROPERTY_3 = 294
    CUSTOM_PROPERTY_4 = 295
    CUSTOM_PROPERTY_5 = 296
    CUSTOM_PROPERTY_6 = 297
    CUSTOM_PROPERTY_7 = 298
    CUSTOM_PROPERTY_8 = 299
    CUSTOM_PROPERTY_9 = 300
    ALLOCATION_SIZE = 301
    SFV_CRC32 = 302
    MD5SUM_MD5 = 303
    SHA1SUM_SHA1 = 304
    SHA256SUM_SHA256 = 305
    SFV_PASS = 306
    MD5SUM_PASS = 307
    SHA1SUM_PASS = 308
    SHA256SUM_PASS = 309
    ALTERNATE_DATA_STREAM_ANSI = 310
    ALTERNATE_DATA_STREAM_UTF8 = 311
    ALTERNATE_DATA_STREAM_UTF16LE = 312
    ALTERNATE_DATA_STREAM_UTF16BE = 313
    ALTERNATE_DATA_STREAM_TEXT_PLAIN = 314
    ALTERNATE_DATA_STREAM_HEX = 315
    PERCEIVED_TYPE = 316
    CONTENT_TYPE = 317
    OPENED_BY = 318
    TARGET_MACHINE = 319
    SHA512SUM_SHA512 = 320
    SHA512SUM_PASS = 321
    PARENT_PATH = 322
    FIRST_256_BYTES = 323
    FIRST_512_BYTES = 324
    LAST_256_BYTES = 325
    LAST_512_BYTES = 326
    INDEX_ONLINE = 327
    COLUMN_0 = 328
    COLUMN_1 = 329
    COLUMN_2 = 330
    COLUMN_3 = 331
    COLUMN_4 = 332
    COLUMN_5 = 333
    COLUMN_6 = 334
    COLUMN_7 = 335
    COLUMN_8 = 336
    COLUMN_9 = 337
    COLUMN_A = 338
    COLUMN_B = 339
    COLUMN_C = 340
    COLUMN_D = 341
    COLUMN_E = 342
    COLUMN_F = 343
    ZONE_ID = 344
    REFERRER_URL = 345
    HOST_URL = 346
    CHARACTER_ENCODING = 347
    ROOT_NAME = 348
    USED_DISK_SIZE = 349
    VOLUME_PATH = 350
    MAX_CHILD_DEPTH = 351
    TOTAL_CHILD_SIZE = 352
    ROW = 353
    CHILD_OCCURRENCE_COUNT = 354
    VOLUME_NAME = 355
    DESCENDANT_OCCURRENCE_COUNT = 356
    OBJECT_ID = 357
    BIRTH_VOLUME_ID = 358
    BIRTH_OBJECT_ID = 359
    DOMAIN_ID = 360
    FOLDER_DATA_CRC32 = 361
    FOLDER_DATA_CRC64 = 362
    FOLDER_DATA_MD5 = 363
    FOLDER_DATA_SHA1 = 364
    FOLDER_DATA_SHA256 = 365
    FOLDER_DATA_SHA512 = 366
    FOLDER_DATA_AND_NAMES_CRC32 = 367
    FOLDER_DATA_AND_NAMES_CRC64 = 368
    FOLDER_DATA_AND_NAMES_MD5 = 369
    FOLDER_DATA_AND_NAMES_SHA1 = 370
    FOLDER_DATA_AND_NAMES_SHA256 = 371
    FOLDER_DATA_AND_NAMES_SHA512 = 372
    FOLDER_NAMES_CRC32 = 373
    FOLDER_NAMES_CRC64 = 374
    FOLDER_NAMES_MD5 = 375
    FOLDER_NAMES_SHA1 = 376
    FOLDER_NAMES_SHA256 = 377
    FOLDER_NAMES_SHA512 = 378
    FOLDER_DATA_CRC32_FROM_DISK = 379
    FOLDER_DATA_CRC64_FROM_DISK = 380
    FOLDER_DATA_MD5_FROM_DISK = 381
    FOLDER_DATA_SHA1_FROM_DISK = 382
    FOLDER_DATA_SHA256_FROM_DISK = 383
    FOLDER_DATA_SHA512_FROM_DISK = 384
    FOLDER_DATA_AND_NAMES_CRC32_FROM_DISK = 385
    FOLDER_DATA_AND_NAMES_CRC64_FROM_DISK = 386
    FOLDER_DATA_AND_NAMES_MD5_FROM_DISK = 387
    FOLDER_DATA_AND_NAMES_SHA1_FROM_DISK = 388
    FOLDER_DATA_AND_NAMES_SHA256_FROM_DISK = 389
    FOLDER_DATA_AND_NAMES_SHA512_FROM_DISK = 390
    FOLDER_NAMES_CRC32_FROM_DISK = 391
    FOLDER_NAMES_CRC64_FROM_DISK = 392
    FOLDER_NAMES_MD5_FROM_DISK = 393
    FOLDER_NAMES_SHA1_FROM_DISK = 394
    FOLDER_NAMES_SHA256_FROM_DISK = 395
    FOLDER_NAMES_SHA512_FROM_DISK = 396
    LONG_NAME = 397
    LONG_FULL_PATH = 398
    DIGITAL_SIGNATURE_NAME = 399
    DIGITAL_SIGNATURE_TIMESTAMP = 400
    AUDIO_TRACK_COUNT = 401
    VIDEO_TRACK_COUNT = 402
    SUBTITLE_TRACK_COUNT = 403
    NETWORK_INDEX_HOST = 404
    ORIGINAL_LOCATION = 405
    DATE_DELETED = 406
    STATUS = 407
    VORBIS_COMMENT = 408
    QUICKTIME_METADATA = 409
    PARENT_SIZE = 410
    ROOT_SIZE = 411
    OPENS_WITH = 412
    RANDOMIZE = 413
    ICON = 414
    THUMBNAIL = 415
    CONTENT = 416
    SEPARATOR = 417

PropertyIdToValueTypeMap = {
    PropertyId.NAME: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.PATH: PropertyType.PSTRING_FOLDER_REFERENCE,
    PropertyId.SIZE: PropertyType.UINT64,
    PropertyId.EXTENSION: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.TYPE: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.DATE_MODIFIED: PropertyType.UINT64,
    PropertyId.DATE_CREATED: PropertyType.UINT64,
    PropertyId.DATE_ACCESSED: PropertyType.UINT64,
    PropertyId.ATTRIBUTES: PropertyType.DWORD,
    PropertyId.DATE_RECENTLY_CHANGED: PropertyType.UINT64,
    PropertyId.RUN_COUNT: PropertyType.DWORD,
    PropertyId.DATE_RUN: PropertyType.UINT64,
    PropertyId.FILE_LIST_FILENAME: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.WIDTH: PropertyType.DWORD,
    PropertyId.HEIGHT: PropertyType.DWORD,
    PropertyId.DIMENSIONS: PropertyType.DIMENSIONS,
    PropertyId.ASPECT_RATIO: PropertyType.DWORD_FIXED_Q1K,
    PropertyId.BIT_DEPTH: PropertyType.BYTE,
    PropertyId.LENGTH: PropertyType.UINT64,
    PropertyId.AUDIO_SAMPLE_RATE: PropertyType.DWORD,
    PropertyId.AUDIO_CHANNELS: PropertyType.DWORD,
    PropertyId.AUDIO_BITS_PER_SAMPLE: PropertyType.DWORD,
    PropertyId.AUDIO_BIT_RATE: PropertyType.DWORD,
    PropertyId.AUDIO_FORMAT: PropertyType.PSTRING,
    PropertyId.FILE_SIGNATURE: PropertyType.DWORD_GET_TEXT,
    PropertyId.TITLE: PropertyType.PSTRING,
    PropertyId.ARTIST: PropertyType.PSTRING_MULTISTRING,
    PropertyId.ALBUM: PropertyType.PSTRING,
    PropertyId.YEAR: PropertyType.DWORD,
    PropertyId.COMMENT: PropertyType.PSTRING,
    PropertyId.TRACK: PropertyType.DWORD,
    PropertyId.GENRE: PropertyType.PSTRING_MULTISTRING,
    PropertyId.FRAME_RATE: PropertyType.DWORD_FIXED_Q1K,
    PropertyId.VIDEO_BIT_RATE: PropertyType.DWORD,
    PropertyId.VIDEO_FORMAT: PropertyType.PSTRING,
    PropertyId.RATING: PropertyType.BYTE,
    PropertyId.TAGS: PropertyType.PSTRING_MULTISTRING,
    PropertyId.MD5: PropertyType.BLOB8,
    PropertyId.SHA1: PropertyType.BLOB8,
    PropertyId.SHA256: PropertyType.BLOB8,
    PropertyId.CRC32: PropertyType.BLOB8,
    PropertyId.SIZE_ON_DISK: PropertyType.UINT64,
    PropertyId.DESCRIPTION: PropertyType.PSTRING,
    PropertyId.VERSION: PropertyType.PSTRING,
    PropertyId.PRODUCT_NAME: PropertyType.PSTRING,
    PropertyId.PRODUCT_VERSION: PropertyType.PSTRING,
    PropertyId.COMPANY: PropertyType.PSTRING,
    PropertyId.KIND: PropertyType.PSTRING,
    PropertyId.FILE_NAME_LENGTH: PropertyType.SIZE_T,
    PropertyId.FULL_PATH_LENGTH: PropertyType.SIZE_T,
    PropertyId.SUBJECT: PropertyType.PSTRING,
    PropertyId.AUTHORS: PropertyType.PSTRING_MULTISTRING,
    PropertyId.DATE_TAKEN: PropertyType.UINT64,
    PropertyId.SOFTWARE: PropertyType.PSTRING,
    PropertyId.DATE_ACQUIRED: PropertyType.UINT64,
    PropertyId.COPYRIGHT: PropertyType.PSTRING,
    PropertyId.IMAGE_ID: PropertyType.PSTRING,
    PropertyId.HORIZONTAL_RESOLUTION: PropertyType.DWORD,
    PropertyId.VERTICAL_RESOLUTION: PropertyType.DWORD,
    PropertyId.COMPRESSION: PropertyType.WORD,
    PropertyId.RESOLUTION_UNIT: PropertyType.BYTE_GET_TEXT,
    PropertyId.COLOR_REPRESENTATION: PropertyType.WORD,
    PropertyId.COMPRESSED_BITS_PER_PIXEL: PropertyType.INT32_FIXED_Q1K,
    PropertyId.CAMERA_MAKER: PropertyType.PSTRING,
    PropertyId.CAMERA_MODEL: PropertyType.PSTRING,
    PropertyId.F_STOP: PropertyType.INT32_FIXED_Q1K,
    PropertyId.EXPOSURE_TIME: PropertyType.INT32_FIXED_Q1K,
    PropertyId.ISO_SPEED: PropertyType.WORD,
    PropertyId.EXPOSURE_BIAS: PropertyType.INT32_FIXED_Q1K,
    PropertyId.FOCAL_LENGTH: PropertyType.INT32_FIXED_Q1K,
    PropertyId.MAX_APERTURE: PropertyType.INT32_FIXED_Q1M,
    PropertyId.METERING_MODE: PropertyType.WORD,
    PropertyId.SUBJECT_DISTANCE: PropertyType.INT32_FIXED_Q1K,
    PropertyId.FLASH_MODE: PropertyType.BYTE_GET_TEXT,
    PropertyId.FLASH_ENERGY: PropertyType.INT32_FIXED_Q1K,
    PropertyId.LENS_MAKER: PropertyType.PSTRING,
    PropertyId.LENS_MODEL: PropertyType.PSTRING,
    PropertyId.FLASH_MAKER: PropertyType.PSTRING,
    PropertyId.FLASH_MODEL: PropertyType.PSTRING,
    PropertyId.CAMERA_SERIAL_NUMBER: PropertyType.PSTRING,
    PropertyId.CONTRAST: PropertyType.DWORD,
    PropertyId.BRIGHTNESS: PropertyType.INT32_FIXED_Q1M,
    PropertyId.LIGHT_SOURCE: PropertyType.DWORD,
    PropertyId.EXPOSURE_PROGRAM: PropertyType.DWORD,
    PropertyId.SATURATION: PropertyType.DWORD,
    PropertyId.SHARPNESS: PropertyType.DWORD,
    PropertyId.WHITE_BALANCE: PropertyType.DWORD,
    PropertyId.PHOTOMETRIC_INTERPRETATION: PropertyType.WORD,
    PropertyId.DIGITAL_ZOOM: PropertyType.INT32_FIXED_Q1K,
    PropertyId.EXIF_VERSION: PropertyType.PSTRING,
    PropertyId.LATITUDE: PropertyType.INT32_FIXED_Q1M,
    PropertyId.LONGITUDE: PropertyType.INT32_FIXED_Q1M,
    PropertyId.ALTITUDE: PropertyType.INT32_FIXED_Q1M,
    PropertyId.SUBTITLE: PropertyType.PSTRING,
    PropertyId.TOTAL_BIT_RATE: PropertyType.DWORD,
    PropertyId.DIRECTORS: PropertyType.PSTRING_MULTISTRING,
    PropertyId.PRODUCERS: PropertyType.PSTRING_MULTISTRING,
    PropertyId.WRITERS: PropertyType.PSTRING_MULTISTRING,
    PropertyId.PUBLISHER: PropertyType.PSTRING,
    PropertyId.CONTENT_DISTRIBUTOR: PropertyType.PSTRING,
    PropertyId.DATE_ENCODED: PropertyType.UINT64,
    PropertyId.ENCODED_BY: PropertyType.PSTRING,
    PropertyId.AUTHOR_URL: PropertyType.PSTRING,
    PropertyId.PROMOTION_URL: PropertyType.PSTRING,
    PropertyId.OFFLINE_AVAILABILITY: PropertyType.DWORD,
    PropertyId.OFFLINE_STATUS: PropertyType.DWORD,
    PropertyId.SHARED_WITH: PropertyType.PSTRING_MULTISTRING,
    PropertyId.OWNER: PropertyType.PSTRING,
    PropertyId.COMPUTER: PropertyType.PSTRING,
    PropertyId.ALBUM_ARTIST: PropertyType.PSTRING,
    PropertyId.PARENTAL_RATING_REASON: PropertyType.PSTRING,
    PropertyId.COMPOSER: PropertyType.PSTRING_MULTISTRING,
    PropertyId.CONDUCTOR: PropertyType.PSTRING,
    PropertyId.CONTENT_GROUP_DESCRIPTION: PropertyType.PSTRING,
    PropertyId.MOOD: PropertyType.PSTRING,
    PropertyId.PART_OF_SET: PropertyType.PSTRING,
    PropertyId.INITIAL_KEY: PropertyType.PSTRING,
    PropertyId.BEATS_PER_MINUTE: PropertyType.PSTRING,
    PropertyId.PROTECTED: PropertyType.BYTE_GET_TEXT,
    PropertyId.PART_OF_A_COMPILATION: PropertyType.BYTE_GET_TEXT,
    PropertyId.PARENTAL_RATING: PropertyType.PSTRING,
    PropertyId.PERIOD: PropertyType.PSTRING,
    PropertyId.PEOPLE: PropertyType.PSTRING_MULTISTRING,
    PropertyId.CATEGORY: PropertyType.PSTRING_MULTISTRING,
    PropertyId.CONTENT_STATUS: PropertyType.PSTRING,
    PropertyId.DOCUMENT_CONTENT_TYPE: PropertyType.PSTRING,
    PropertyId.PAGE_COUNT: PropertyType.DWORD,
    PropertyId.WORD_COUNT: PropertyType.DWORD,
    PropertyId.CHARACTER_COUNT: PropertyType.DWORD,
    PropertyId.LINE_COUNT: PropertyType.DWORD,
    PropertyId.PARAGRAPH_COUNT: PropertyType.DWORD,
    PropertyId.TEMPLATE: PropertyType.PSTRING,
    PropertyId.SCALE: PropertyType.BYTE_GET_TEXT,
    PropertyId.LINKS_DIRTY: PropertyType.BYTE_GET_TEXT,
    PropertyId.LANGUAGE: PropertyType.PSTRING,
    PropertyId.LAST_AUTHOR: PropertyType.PSTRING,
    PropertyId.REVISION_NUMBER: PropertyType.PSTRING,
    PropertyId.VERSION_NUMBER: PropertyType.PSTRING,
    PropertyId.MANAGER: PropertyType.PSTRING,
    PropertyId.DATE_CONTENT_CREATED: PropertyType.UINT64,
    PropertyId.DATE_SAVED: PropertyType.UINT64,
    PropertyId.DATE_PRINTED: PropertyType.UINT64,
    PropertyId.TOTAL_EDITING_TIME: PropertyType.UINT64,
    PropertyId.ORIGINAL_FILE_NAME: PropertyType.PSTRING,
    PropertyId.DATE_RELEASED: PropertyType.PSTRING,
    PropertyId.SLIDE_COUNT: PropertyType.DWORD,
    PropertyId.NOTE_COUNT: PropertyType.DWORD,
    PropertyId.HIDDEN_SLIDE_COUNT: PropertyType.DWORD,
    PropertyId.PRESENTATION_FORMAT: PropertyType.PSTRING,
    PropertyId.TRADEMARKS: PropertyType.PSTRING,
    PropertyId.DISPLAY_NAME: PropertyType.PSTRING,
    PropertyId.FILE_NAME_LENGTH_IN_UTF8_BYTES: PropertyType.SIZE_T,
    PropertyId.FULL_PATH_LENGTH_IN_UTF8_BYTES: PropertyType.SIZE_T,
    PropertyId.CHILD_COUNT: PropertyType.SIZE_T,
    PropertyId.CHILD_FOLDER_COUNT: PropertyType.SIZE_T,
    PropertyId.CHILD_FILE_COUNT: PropertyType.SIZE_T,
    PropertyId.CHILD_COUNT_FROM_DISK: PropertyType.SIZE_T,
    PropertyId.CHILD_FOLDER_COUNT_FROM_DISK: PropertyType.SIZE_T,
    PropertyId.CHILD_FILE_COUNT_FROM_DISK: PropertyType.SIZE_T,
    PropertyId.FOLDER_DEPTH: PropertyType.SIZE_T,
    PropertyId.TOTAL_SIZE: PropertyType.UINT64,
    PropertyId.TOTAL_SIZE_ON_DISK: PropertyType.UINT64,
    PropertyId.DATE_CHANGED: PropertyType.UINT64,
    PropertyId.HARD_LINK_COUNT: PropertyType.DWORD,
    PropertyId.DELETE_PENDING: PropertyType.BYTE_GET_TEXT,
    PropertyId.IS_DIRECTORY: PropertyType.BYTE_GET_TEXT,
    PropertyId.ALTERNATE_DATA_STREAM_COUNT: PropertyType.DWORD,
    PropertyId.ALTERNATE_DATA_STREAM_NAMES: PropertyType.PSTRING_MULTISTRING,
    PropertyId.TOTAL_ALTERNATE_DATA_STREAM_SIZE: PropertyType.UINT64,
    PropertyId.TOTAL_ALTERNATE_DATA_STREAM_SIZE_ON_DISK: PropertyType.UINT64,
    PropertyId.COMPRESSED_SIZE: PropertyType.UINT64,
    PropertyId.COMPRESSION_FORMAT: PropertyType.WORD,
    PropertyId.COMPRESSION_UNIT_SHIFT: PropertyType.BYTE,
    PropertyId.COMPRESSION_CHUNK_SHIFT: PropertyType.BYTE,
    PropertyId.COMPRESSION_CLUSTER_SHIFT: PropertyType.BYTE,
    PropertyId.COMPRESSION_RATIO: PropertyType.BYTE,
    PropertyId.REPARSE_TAG: PropertyType.DWORD,
    PropertyId.REMOTE_PROTOCOL: PropertyType.DWORD,
    PropertyId.REMOTE_PROTOCOL_VERSION: PropertyType.PSTRING,
    PropertyId.REMOTE_PROTOCOL_FLAGS: PropertyType.DWORD,
    PropertyId.LOGICAL_BYTES_PER_SECTOR: PropertyType.DWORD,
    PropertyId.PHYSICAL_BYTES_PER_SECTOR_FOR_ATOMICITY: PropertyType.DWORD,
    PropertyId.PHYSICAL_BYTES_PER_SECTOR_FOR_PERFORMANCE: PropertyType.DWORD,
    PropertyId.EFFECTIVE_PHYSICAL_BYTES_PER_SECTOR_FOR_ATOMICITY: PropertyType.DWORD,
    PropertyId.FILE_STORAGE_INFO_FLAGS: PropertyType.DWORD,
    PropertyId.BYTE_OFFSET_FOR_SECTOR_ALIGNMENT: PropertyType.DWORD,
    PropertyId.BYTE_OFFSET_FOR_PARTITION_ALIGNMENT: PropertyType.DWORD,
    PropertyId.ALIGNMENT_REQUIREMENT: PropertyType.DWORD,
    PropertyId.VOLUME_SERIAL_NUMBER: PropertyType.UINT64,
    PropertyId.FILE_ID: PropertyType.UINT128,
    PropertyId.FRAME_COUNT: PropertyType.DWORD,
    PropertyId.CLUSTER_SIZE: PropertyType.DWORD,
    PropertyId.SECTOR_SIZE: PropertyType.DWORD,
    PropertyId.AVAILABLE_FREE_DISK_SIZE: PropertyType.UINT64,
    PropertyId.FREE_DISK_SIZE: PropertyType.UINT64,
    PropertyId.TOTAL_DISK_SIZE: PropertyType.UINT64,
    PropertyId.MAXIMUM_COMPONENT_LENGTH: PropertyType.DWORD,
    PropertyId.FILE_SYSTEM_FLAGS: PropertyType.DWORD,
    PropertyId.FILE_SYSTEM: PropertyType.PSTRING,
    PropertyId.ORIENTATION: PropertyType.WORD,
    PropertyId.END_OF_FILE: PropertyType.UINT64,
    PropertyId.SHORT_NAME: PropertyType.PSTRING,
    PropertyId.SHORT_FULL_PATH: PropertyType.PSTRING,
    PropertyId.ENCRYPTION_STATUS: PropertyType.DWORD,
    PropertyId.HARD_LINK_FILE_NAMES: PropertyType.PSTRING_MULTISTRING,
    PropertyId.INDEX_TYPE: PropertyType.BYTE_GET_TEXT,
    PropertyId.DRIVE_TYPE: PropertyType.DWORD,
    PropertyId.BINARY_TYPE: PropertyType.DWORD,
    PropertyId.REGEX_MATCH_0: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_1: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_2: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_3: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_4: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_5: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_6: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_7: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_8: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.REGEX_MATCH_9: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.SIBLING_COUNT: PropertyType.SIZE_T,
    PropertyId.SIBLING_FOLDER_COUNT: PropertyType.SIZE_T,
    PropertyId.SIBLING_FILE_COUNT: PropertyType.SIZE_T,
    PropertyId.INDEX_NUMBER: PropertyType.SIZE_T,
    PropertyId.SHORTCUT_TARGET: PropertyType.PSTRING,
    PropertyId.OUT_OF_DATE: PropertyType.BYTE_GET_TEXT,
    PropertyId.INCUR_SEEK_PENALTY: PropertyType.BYTE_GET_TEXT,
    PropertyId.PLAIN_TEXT_LINE_COUNT: PropertyType.DWORD,
    PropertyId.APERTURE: PropertyType.INT32_FIXED_Q1M,
    PropertyId.MAKER_NOTE: PropertyType.PSTRING,
    PropertyId.RELATED_SOUND_FILE: PropertyType.PSTRING,
    PropertyId.SHUTTER_SPEED: PropertyType.INT32_FIXED_Q1K,
    PropertyId.TRANSCODED_FOR_SYNC: PropertyType.BYTE_GET_TEXT,
    PropertyId.CASE_SENSITIVE_DIR: PropertyType.BYTE_GET_TEXT,
    PropertyId.DATE_INDEXED: PropertyType.UINT64,
    PropertyId.NAME_FREQUENCY: PropertyType.SIZE_T,
    PropertyId.SIZE_FREQUENCY: PropertyType.SIZE_T,
    PropertyId.EXTENSION_FREQUENCY: PropertyType.SIZE_T,
    PropertyId.REGEX_MATCHES: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.URL: PropertyType.PSTRING,
    PropertyId.FULL_PATH: PropertyType.PSTRING_FILE_OR_FOLDER_REFERENCE,
    PropertyId.PARENT_FILE_ID: PropertyType.UINT128,
    PropertyId.SHA512: PropertyType.BLOB8,
    PropertyId.SHA384: PropertyType.BLOB8,
    PropertyId.CRC64: PropertyType.BLOB8,
    PropertyId.FIRST_BYTE: PropertyType.BLOB8,
    PropertyId.FIRST_2_BYTES: PropertyType.BLOB8,
    PropertyId.FIRST_4_BYTES: PropertyType.BLOB8,
    PropertyId.FIRST_8_BYTES: PropertyType.BLOB8,
    PropertyId.FIRST_16_BYTES: PropertyType.BLOB8,
    PropertyId.FIRST_32_BYTES: PropertyType.BLOB8,
    PropertyId.FIRST_64_BYTES: PropertyType.BLOB8,
    PropertyId.FIRST_128_BYTES: PropertyType.BLOB8,
    PropertyId.LAST_BYTE: PropertyType.BLOB8,
    PropertyId.LAST_2_BYTES: PropertyType.BLOB8,
    PropertyId.LAST_4_BYTES: PropertyType.BLOB8,
    PropertyId.LAST_8_BYTES: PropertyType.BLOB8,
    PropertyId.LAST_16_BYTES: PropertyType.BLOB8,
    PropertyId.LAST_32_BYTES: PropertyType.BLOB8,
    PropertyId.LAST_64_BYTES: PropertyType.BLOB8,
    PropertyId.LAST_128_BYTES: PropertyType.BLOB8,
    PropertyId.BYTE_ORDER_MARK: PropertyType.BYTE_GET_TEXT,
    PropertyId.VOLUME_LABEL: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.FILE_LIST_FULL_PATH: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.DISPLAY_FULL_PATH: PropertyType.PSTRING,
    PropertyId.PARSE_NAME: PropertyType.PSTRING,
    PropertyId.PARSE_FULL_PATH: PropertyType.PSTRING,
    PropertyId.STEM: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.SHELL_ATTRIBUTES: PropertyType.DWORD,
    PropertyId.IS_FOLDER: PropertyType.BYTE_GET_TEXT,
    PropertyId.VALID_UTF8: PropertyType.BYTE_GET_TEXT,
    PropertyId.STEM_LENGTH: PropertyType.SIZE_T,
    PropertyId.EXTENSION_LENGTH: PropertyType.SIZE_T,
    PropertyId.PATH_PART_LENGTH: PropertyType.SIZE_T,
    PropertyId.TIME_MODIFIED: PropertyType.DWORD,
    PropertyId.TIME_CREATED: PropertyType.DWORD,
    PropertyId.TIME_ACCESSED: PropertyType.DWORD,
    PropertyId.DAY_MODIFIED: PropertyType.DWORD,
    PropertyId.DAY_CREATED: PropertyType.DWORD,
    PropertyId.DAY_ACCESSED: PropertyType.DWORD,
    PropertyId.PARENT_NAME: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.REPARSE_TARGET: PropertyType.PSTRING,
    PropertyId.DESCENDANT_COUNT: PropertyType.SIZE_T,
    PropertyId.DESCENDANT_FOLDER_COUNT: PropertyType.SIZE_T,
    PropertyId.DESCENDANT_FILE_COUNT: PropertyType.SIZE_T,
    PropertyId.FROM: PropertyType.PSTRING,
    PropertyId.TO: PropertyType.PSTRING_MULTISTRING,
    PropertyId.DATE_RECEIVED: PropertyType.UINT64,
    PropertyId.DATE_SENT: PropertyType.UINT64,
    PropertyId.CONTAINER_FILENAMES: PropertyType.PSTRING_MULTISTRING,
    PropertyId.CONTAINER_FILE_COUNT: PropertyType.DWORD,
    PropertyId.CUSTOM_PROPERTY_0: PropertyType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_1: PropertyType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_2: PropertyType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_3: PropertyType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_4: PropertyType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_5: PropertyType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_6: PropertyType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_7: PropertyType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_8: PropertyType.PSTRING,
    PropertyId.CUSTOM_PROPERTY_9: PropertyType.PSTRING,
    PropertyId.ALLOCATION_SIZE: PropertyType.UINT64,
    PropertyId.SFV_CRC32: PropertyType.BLOB8,
    PropertyId.MD5SUM_MD5: PropertyType.BLOB8,
    PropertyId.SHA1SUM_SHA1: PropertyType.BLOB8,
    PropertyId.SHA256SUM_SHA256: PropertyType.BLOB8,
    PropertyId.SFV_PASS: PropertyType.BYTE_GET_TEXT,
    PropertyId.MD5SUM_PASS: PropertyType.BYTE_GET_TEXT,
    PropertyId.SHA1SUM_PASS: PropertyType.BYTE_GET_TEXT,
    PropertyId.SHA256SUM_PASS: PropertyType.BYTE_GET_TEXT,
    PropertyId.ALTERNATE_DATA_STREAM_ANSI: PropertyType.PSTRING_MULTISTRING,
    PropertyId.ALTERNATE_DATA_STREAM_UTF8: PropertyType.PSTRING_MULTISTRING,
    PropertyId.ALTERNATE_DATA_STREAM_UTF16LE: PropertyType.PSTRING_MULTISTRING,
    PropertyId.ALTERNATE_DATA_STREAM_UTF16BE: PropertyType.PSTRING_MULTISTRING,
    PropertyId.ALTERNATE_DATA_STREAM_TEXT_PLAIN: PropertyType.PSTRING_MULTISTRING,
    PropertyId.ALTERNATE_DATA_STREAM_HEX: PropertyType.PSTRING_MULTISTRING,
    PropertyId.PERCEIVED_TYPE: PropertyType.PSTRING,
    PropertyId.CONTENT_TYPE: PropertyType.PSTRING,
    PropertyId.OPENED_BY: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.TARGET_MACHINE: PropertyType.WORD_GET_TEXT,
    PropertyId.SHA512SUM_SHA512: PropertyType.BLOB8,
    PropertyId.SHA512SUM_PASS: PropertyType.BYTE_GET_TEXT,
    PropertyId.PARENT_PATH: PropertyType.PSTRING_FOLDER_REFERENCE,
    PropertyId.FIRST_256_BYTES: PropertyType.BLOB16,
    PropertyId.FIRST_512_BYTES: PropertyType.BLOB16,
    PropertyId.LAST_256_BYTES: PropertyType.BLOB16,
    PropertyId.LAST_512_BYTES: PropertyType.BLOB16,
    PropertyId.INDEX_ONLINE: PropertyType.BYTE_GET_TEXT,
    PropertyId.COLUMN_0: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_1: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_2: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_3: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_4: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_5: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_6: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_7: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_8: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_9: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_A: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_B: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_C: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_D: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_E: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.COLUMN_F: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.ZONE_ID: PropertyType.BYTE_GET_TEXT,
    PropertyId.REFERRER_URL: PropertyType.PSTRING,
    PropertyId.HOST_URL: PropertyType.PSTRING,
    PropertyId.CHARACTER_ENCODING: PropertyType.BYTE_GET_TEXT,
    PropertyId.ROOT_NAME: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.USED_DISK_SIZE: PropertyType.UINT64,
    PropertyId.VOLUME_PATH: PropertyType.PSTRING,
    PropertyId.MAX_CHILD_DEPTH: PropertyType.SIZE_T,
    PropertyId.TOTAL_CHILD_SIZE: PropertyType.UINT64,
    PropertyId.ROW: PropertyType.SIZE_T,
    PropertyId.CHILD_OCCURRENCE_COUNT: PropertyType.SIZE_T,
    PropertyId.VOLUME_NAME: PropertyType.PSTRING,
    PropertyId.DESCENDANT_OCCURRENCE_COUNT: PropertyType.SIZE_T,
    PropertyId.OBJECT_ID: PropertyType.BLOB8,
    PropertyId.BIRTH_VOLUME_ID: PropertyType.BLOB8,
    PropertyId.BIRTH_OBJECT_ID: PropertyType.BLOB8,
    PropertyId.DOMAIN_ID: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_CRC32: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_CRC64: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_MD5: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_SHA1: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_SHA256: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_SHA512: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_CRC32: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_CRC64: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_MD5: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_SHA1: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_SHA256: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_SHA512: PropertyType.BLOB8,
    PropertyId.FOLDER_NAMES_CRC32: PropertyType.BLOB8,
    PropertyId.FOLDER_NAMES_CRC64: PropertyType.BLOB8,
    PropertyId.FOLDER_NAMES_MD5: PropertyType.BLOB8,
    PropertyId.FOLDER_NAMES_SHA1: PropertyType.BLOB8,
    PropertyId.FOLDER_NAMES_SHA256: PropertyType.BLOB8,
    PropertyId.FOLDER_NAMES_SHA512: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_CRC32_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_CRC64_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_MD5_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_SHA1_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_SHA256_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_SHA512_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_CRC32_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_CRC64_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_MD5_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_SHA1_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_SHA256_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_DATA_AND_NAMES_SHA512_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_NAMES_CRC32_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_NAMES_CRC64_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_NAMES_MD5_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_NAMES_SHA1_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_NAMES_SHA256_FROM_DISK: PropertyType.BLOB8,
    PropertyId.FOLDER_NAMES_SHA512_FROM_DISK: PropertyType.BLOB8,
    PropertyId.LONG_NAME: PropertyType.PSTRING,
    PropertyId.LONG_FULL_PATH: PropertyType.PSTRING,
    PropertyId.DIGITAL_SIGNATURE_NAME: PropertyType.PSTRING,
    PropertyId.DIGITAL_SIGNATURE_TIMESTAMP: PropertyType.UINT64,
    PropertyId.AUDIO_TRACK_COUNT: PropertyType.DWORD,
    PropertyId.VIDEO_TRACK_COUNT: PropertyType.DWORD,
    PropertyId.SUBTITLE_TRACK_COUNT: PropertyType.DWORD,
    PropertyId.NETWORK_INDEX_HOST: PropertyType.PSTRING_STRING_REFERENCE,
    PropertyId.ORIGINAL_LOCATION: PropertyType.PSTRING,
    PropertyId.DATE_DELETED: PropertyType.UINT64,
    PropertyId.STATUS: PropertyType.BYTE,
    PropertyId.VORBIS_COMMENT: PropertyType.PSTRING_MULTISTRING,
    PropertyId.QUICKTIME_METADATA: PropertyType.PSTRING_MULTISTRING,
    PropertyId.PARENT_SIZE: PropertyType.UINT64,
    PropertyId.ROOT_SIZE: PropertyType.UINT64,
    PropertyId.OPENS_WITH: PropertyType.PSTRING,
    PropertyId.RANDOMIZE: PropertyType.SIZE_T,
    PropertyId.ICON: PropertyType.NULL,
    PropertyId.THUMBNAIL: PropertyType.NULL,
    PropertyId.CONTENT: PropertyType.PSTRING,
    PropertyId.SEPARATOR: PropertyType.NULL,
}
def PropertyIdToValueType(id: PropertyId) -> typing.Optional[PropertyType]:
    return PropertyIdToValueTypeMap.get(id, None)
#endregion

