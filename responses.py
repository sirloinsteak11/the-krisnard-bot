from api import get_random_tweet, get_random_gelbooru


async def handle_response(message):
  p_message = message.lower()
  if p_message == '!s':
    return await get_random_tweet()

  if '!gel' in p_message:
    return await get_random_gelbooru(p_message)

  if p_message == '!helpme':
    return '!s - spits out random liked posts from krisnards twitter account\n!gel (tags) - searches random gelbooru image with the specified tags. if no results are found use different variations. multiple tags allowed. if no tags specified, it will spit out a completely random image'
  return ''
