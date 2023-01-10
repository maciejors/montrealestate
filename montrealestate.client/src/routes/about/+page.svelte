<svelte:head>
  <title>About us - montrealestate</title>
  Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta, magnam fuga dolore facilis earum officia eum officiis dolorum sapiente sint veniam? Quasi fugiat eum exercitationem facere. Totam quas quibusdam porro.
</svelte:head>

<script lang="ts">
  import Container from "../../components/Container.svelte";

  interface UserComment {
    userName: string;
    userBio: string;
    imgUrl: string;
    comment: string;
  }
  const userComments: UserComment[] = [
    { 
      userName: 'Mason Mount',
      userBio: 'Footballer for Chelsea FC',
      imgUrl: 'https://media.discordapp.net/attachments/504576727461134338/1062427842719264791/image.png',
      comment: 'Buying a stadium has never been this seamless!',
    },
    { 
      userName: 'Obi-Wan Kenobi',
      userBio: 'Jedi Master',
      imgUrl: 'https://media.discordapp.net/attachments/504576727461134338/1062430422891511910/image.png',
      comment: 'The best property webiste in this part of the galaxy.',
    },
    { 
      userName: 'Stella',
      userBio: 'A cute dog',
      imgUrl: 'https://cdn.discordapp.com/attachments/504576727461134338/1062421944160497734/image.png',
      comment: 'Superb website!  Yesterday I bought myself a roomy kennel in Montreal!',
    },
    { 
      userName: 'Anonymous',
      userBio: 'totally not a designer of this website',
      imgUrl: 'https://media.discordapp.net/attachments/504576727461134338/1062428945473085450/image.png',
      comment: '10/10! The website has a very clean and modern look. It is also responsive - I can browse properties on my phone without any issues! Motlo bene!!!',
    },
  ]
</script>

<Container>
  <div class="card flex flex-col items-center max-w-lg text-justify p-8 my-10 cool-animation">
    <h1 class="text-3xl mb-4">About us</h1>
    <p>The best Montreal property website ever</p>
    <p>Seriously c:</p>
    <p>We stole the data from <a class="text-primary border-b border-transparent hover:border-primary" href="https://github.com/npow/centris">these guys</a></p>
    <p>Here's some lorem:</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas quos, veritatis molestiae quis similique culpa commodi eum, tempore velit debitis minus ut libero facilis! Mollitia ea sequi quos eligendi reprehenderit!</p>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis, et nisi? Quis corporis, aut culpa voluptatum eaque quas. Minima quaerat dolorum incidunt alias quis veritatis odio dolorem molestiae repudiandae earum?</p>
  </div>
</Container>
<div class="bg-gray-200 pt-6 pb-10">
  <Container>
    <div class="opacity-0 cool-animation">
      <h3 class="text-2xl mb-4 text-center">Hear from our users and partners:</h3>
      <section class="grid grid-cols-1 xl:grid-cols-2 gap-4">
        {#each userComments as userComment}
          <div class="card p-4">
            <header class="flex flex-col border-b border-gray-300 pb-2 mb-2 gap-y-2
              md:border-b-0 md:flex-row md:items-center md:gap-x-4 md:pb-0"
            >
              <div class="col-span-3 rounded-full overflow-hidden w-20 h-fit">
                <img src={userComment.imgUrl} alt={userComment.userName}>
              </div>
              <div class="col-span-9 flex flex-col justify-center">
                <h5 class="text-xl font-bold">{ userComment.userName }</h5>
                <h6 class="text-lg text-gray-500">{ userComment.userBio }</h6>
              </div>
            </header>
            <p>{ userComment.comment }</p>
          </div>
        {/each}
      </section>
    </div>
  </Container>
</div>

<style lang="postcss">
  .cool-animation {
    animation: 1s ease-out 0s forwards cool-animation;
  }
  @keyframes cool-animation {
    0% {
      opacity: 0;
      transform: translateY(-20px);
    }
    100% {
      opacity: 1;
      transform: translateY(0);
    }
  }
</style>