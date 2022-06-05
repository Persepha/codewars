function formatDuration (seconds) {
    if (seconds === 0)
        return 'now'

    duration = {
        year: Math.floor(seconds / (60 * 60 * 24 * 365)),
        day: Math.floor(seconds / (60 * 60 * 24)) % 365,
        hour: Math.floor(seconds / (60 * 60)) % 24,
        minute: Math.floor(seconds /  60) % 60,
        second: seconds %  60,
    }

    components = Object.entries(duration)
                .filter( ([key, value]) => value > 0 )
                .map( ([key, value]) => `${value} ${key}` + (value > 1 ? 's' : ''))

    if (components.length > 1) {
        lastComponent = components.splice(-1, 1)
        return components.join(', ') + ` and ${lastComponent}`
    }

    return components.join(', ')
}
