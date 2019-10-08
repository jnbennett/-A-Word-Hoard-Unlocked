axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
Vue.component('multiselect', window.VueMultiselect.default)

const app = new Vue({
	el: '#app',
	delimiters: ['${', '}'],
	data: {
		message: 'A Word-Hoard Unlocked',
		word: '',
		author: [],
		text:[],
		timePeriod:[],
		searchDisplay: {},
		words: [],
		texts: [],
		authors: [],
		timePeriods: [],
		currentTexts:[],
		currentAuthors:[],
		searchType: 'Phrase',
		phrase: [],
	},
	methods: {

		grabAuthor: async function(){
			const response = await axios.get('api/authors/')
			let authorList = response.data

			this.authors = authorList.map( (elem) => ({
				'first_name':elem['first_name'],
				'last_name': elem['last_name'], 
				'texts':elem['texts'],
				'pk':elem['pk'],
				'value': elem
			}))
		},

		authorLabel({first_name, last_name}){
			return `${first_name} ${last_name}`
		},

		getAuthors: function(){
			this.$nextTick(()=>{
				const timeP = this.texts.filter((text)=>this.timePeriod.includes(text.time_period))		
				
				const authTimePeriod = timeP.map(auth=>auth.time_period)
							
				const updatedAuthors = this.texts.filter((text)=>this.timePeriod.includes(text.time_period))
				
				const authPK = updatedAuthors.map(auth=>auth.author)

				this.currentAuthors = this.authors.filter((auth)=>authPK.includes(auth.pk))


				if(this.timePeriod == 0){
					this.currentAuthors = this.authors
				}



				// this.author = this.texts.filter((auth)=>authorTimePeriod.includes(auth.time_period))
			})
		},

		getTexts: function() {
			this.$nextTick(()=>{

			let authorPks = this.author.map(auth => auth.pk);
			updatedTimePeriod = this.texts.filter((text)=>this.timePeriod.includes(text.time_period))
			let textTimePeriod = updatedTimePeriod.map(text=>text.time_period)
			
		
			// write conditionals to run whether time period or author is selected
			if (this.timePeriod != 0){
				this.currentTexts = this.texts.filter((text)=>textTimePeriod.includes(text.time_period))
				
			}

			else {
			 	this.currentTexts = this.texts
			 }


			if (this.author != 0){
				this.currentTexts = this.texts.filter((text)=>authorPks.includes(text.author));
			}

			});
			
			// this.texts = this.texts.filter(text => this.author) 
			// 	this.authors.map((author) => author.pk)
			// 	.includes(text.author)

			// let filteredList = this.texts.map(function(text){
			// 	return {author: text['author'], title: text['title']}
			// }).filter((text) => text.author == this.author)

			// let x = this.texts.map((text) => ({
			// 	'author': text['author'],
			// 	'title': text['title']
			// 	}))
			// .filter((text) => text.author)
			// console.log(x)
		},

		grabText: async function(){
			const response = await axios.get('api/texts/')
			let textList = response.data

			this.texts = textList.map( (elem) => ({
				'title':elem['title'],
				'author':elem['author'],
				'pk':elem['pk'],
				'time_period': elem['time_period'],
				'value': elem
			}))

			this.grabTimePeriod();

			if (this.author == 0){
			 	this.currentTexts = this.texts
			}
		},


		textLabel({title}){
			return `${title}`
		},

		grabTimePeriod(){
			const periods = this.texts.map(period => period.time_period)
			this.timePeriods = [...new Set(periods)]	
		
		},

		timePeriodLabel(period){
			return `${period}`
		},

		searchWords: async function(){

           // POST words

       		const query = {
       			word: this.word,
       			author: this.author,
       			text: this.text,
       			time_period: this.timePeriod,
       			search_type: this.searchType
       		}

       		const res = await axios.post('search/', query)
       			console.log(res)
       		   this.searchDisplay = res.data


       		  if (this.searchType === 'Phrase'){


				for (let text of this.searchDisplay){
					
					this.boldPhrase(text.sentences)

				}
       		  }

		},

		boldPhrase(texts){
			const phrase = this.word
			const phraseList = phrase.split(' ')
		
			// this.phrase = texts.map((sentence) => {
			// 	const words = sentence.split(' ')
			// 	return words.map((word, i) => ({
			// 		class: (phraseList.join(' ') === [words[i]+' '+words[i+1]] ? 'red' : null),
			// 		word: word
			// 	}))
			// })
			
			for (sentences of texts){
				const sentenceTokens = sentences.toLowerCase().split(' ')	
				const sentence = []
				
				let i = 0
				
				while (i < sentenceTokens.length-phraseList.length+1) {
	    			const wordTokens = sentenceTokens.slice(i, i+phraseList.length)
	    			const phrase = wordTokens.join(' ')
	    			if (JSON.stringify(phraseList) === JSON.stringify(wordTokens)) {
	    				for (let j=0; j<phraseList.length; j++) {
	    					sentence.push({class: 'red', word: wordTokens[j]})
	    					i += phraseList.length
	    				}
	    			} else {
	    				sentence.push({class: '', word: wordTokens[0]})
	    				i++
	    			}
	 
	    		
	    			
				}
				this.phrase.push(sentence)
				console.log(this.phrase)
			}
			
		},
	},

	mounted(){
		this.grabAuthor()
		this.grabText()
	},

})