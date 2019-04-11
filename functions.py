def getUrlFromMediaId(media_id):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
    shortened_id = ''

    while media_id > 0:
        remainder = media_id % 64
        media_id = (media_id - remainder) // 64
        shortened_id = alphabet[int(remainder)] + shortened_id

    return 'https://instagram.com/p/' + shortened_id + '/'
